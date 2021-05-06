set -ex

export ETH_RPC_URL="https://mainnet.infura.io/v3/feb228261711453d992038ab7aebefe3" 
MAINNET_DEBT=$(seth call 0x12c815b0c404D66Dd0491f4EC62839904cec25e7 'currentDebt()(uint256,bool)' | head -n1)

export ETH_RPC_URL="http://localhost:8545" 
LOCAL_DEBT=$(seth call 0x12c815b0c404D66Dd0491f4EC62839904cec25e7 'currentDebt()(uint256,bool)' | head -n1)

echo "scale=16; $MAINNET_DEBT / $LOCAL_DEBT" | bc