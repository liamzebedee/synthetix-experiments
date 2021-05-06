set -ex

export ETH_RPC_URL="https://mainnet.infura.io/v3/feb228261711453d992038ab7aebefe3" 
MAINNET_DEBT=$(seth call 0x12c815b0c404D66Dd0491f4EC62839904cec25e7 'currentDebt()(uint256,bool)' | head -n1)

export ETH_RPC_URL="http://localhost:8545"
DEBT_CACHE=`cat /Users/liamz/Documents/Work/2021_Synthetix/code/synthetix/publish/deployed/mainnet/deployment.json | jq -r .targets.DebtCache.address` 
LOCAL_DEBT=$(seth call $DEBT_CACHE 'currentDebt()(uint256,bool)' | head -n1)

echo "scale=16; $MAINNET_DEBT / $LOCAL_DEBT" | bc

echo Non snX backed debt: $(seth call $DEBT_CACHE 'totalNonSnxBackedDebt()(uint)' | seth --from-wei | LC_NUMERIC=en_US xargs printf "%'.f\n")