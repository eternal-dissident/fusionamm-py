# worker.py
from pathlib import Path
import json
import base58
from fusionamm.program_id import FUSIONAMM_PROGRAM_ADDRESS 

# Constants
FUSIONAMM_PROGRAM_ADDRESS = str(FUSIONAMM_PROGRAM_ADDRESS)
JITO_WALLETS = set([
  "96gYZGLnJYVFmbjzopPSU6QiEV5fGqZNyN9nmNhvrZU5",
  "HFqU5x63VTqvQss8hp11i4wVV8bD44PvwucfZ2bU7gRe",
  "Cw8CFyM9FkoMi7K7Crf6HNQqf4uEMzpKw6QNghXLvLkY",
  "ADaUMid9yfUytqMBgopwjb2DTLSokTSzL1zt6iGPaS49",
  "DfXygSm4jCyNCybVYYK6DwvWqjKee8pbDmJGcLWNDXjh",
  "ADuUkR4vqLUMWXxW9gh6D6L8pMSawimctcNZ5pGwDcEt",
  "DttWaMuVvTiduZRnguLF7jNxTgiMBZ1hyAumKUiL2KRL",
  "3AVi9Tg9Uo68tJfuvoKvqKNWKkC5wPdSSdeBnizKZ6jT",
])

# Load IDL and Map Discriminators

IDL = json.loads(Path("fusionamm/idl.json").read_text())["instructions"]
INSTRUCTIONS = {}
for i in IDL:
    INSTRUCTIONS[i["name"]] = {
        "discriminator": i['discriminator'],
        "accounts": [ii['name'] for ii in i["accounts"]],
    }

DISC_TO_NAME = {
    tuple(v['discriminator']): k 
    for k, v in INSTRUCTIONS.items()
}


def parse_ix_name(data_str: str) -> str:
    """Decodes base58 data and looks up the discriminator."""
    if not data_str:
        return None
    try:
        data_bytes = base58.b58decode(data_str)
        discriminator = tuple(data_bytes[:8])
        return DISC_TO_NAME.get(discriminator)
    except Exception:
        return None

def process_file(path: str):
    p = Path(path)
    txs = json.loads(p.read_text())

    metas = []
    ixs_filtered = []

    for tx in txs:
        # Metadata
        acct_keys = tx['transaction']['message']['accountKeys']
        if len(acct_keys) > 0 and isinstance(acct_keys[0], dict):
             tx_accounts_set = {i['pubkey'] for i in acct_keys}
        else:
             tx_accounts_set = set(acct_keys)

        meta = {
            'tx_signature': tx['transaction']['signatures'][0],
            'tx_slot': tx['slot'],
            'tx_version': tx['version'],
            'tx_block_time': tx['blockTime'],
            'tx_fee': tx['meta']['fee'],
            'tx_cu_consumed': tx['meta']['computeUnitsConsumed'],
            'tx_is_jito': not JITO_WALLETS.isdisjoint(tx_accounts_set),
        }
        metas.append(meta)

        base_ix_info = {
            'tx_signature': meta['tx_signature'],
            'tx_slot': meta['tx_slot'],
            'tx_version': meta['tx_version'],
            'tx_block_time': meta['tx_block_time'],
        }

        # Outer Instructions
        raw_ixs = tx['transaction']['message']['instructions']
        for i, ix in enumerate(raw_ixs):
            # Check Program ID match
            if ix['programId'] == FUSIONAMM_PROGRAM_ADDRESS:
                ix_name = parse_ix_name(ix.get('data', ''))
                
                ixs_filtered.append({
                    **base_ix_info,
                    'ix_level': 'outer',
                    'ix_index': i,
                    'ix_inner_index': None,
                    'ix_program_id': ix['programId'],
                    'ix_accounts': ix.get('accounts', []),
                    'ix_data': ix.get('data', ''),
                    'ix_parsed': ix.get('parsed', {}),
                    'ix_stack_height': ix.get('stackHeight'),
                    'ix_name': ix_name # Might be None, filter later
                })

        # Inner Instructions
        if 'innerInstructions' in tx['meta'] and tx['meta']['innerInstructions']:
            inner_groups = tx['meta']['innerInstructions']
            for inner_group in inner_groups:
                parent_ix_index = inner_group['index']
                
                for k, ix in enumerate(inner_group['instructions']):
                    if ix['programId'] == FUSIONAMM_PROGRAM_ADDRESS:
                        ix_name = parse_ix_name(ix.get('data', ''))
                        
                        ixs_filtered.append({
                            **base_ix_info,
                            'ix_level': 'inner',
                            'ix_index': parent_ix_index,
                            'ix_inner_index': k,
                            'ix_program_id': ix['programId'],
                            'ix_accounts': ix.get('accounts', []),
                            'ix_data': ix.get('data', ''),
                            'ix_parsed': ix.get('parsed', {}),
                            'ix_stack_height': ix.get('stackHeight'),
                            'ix_name': ix_name 
                        })

    return metas, ixs_filtered