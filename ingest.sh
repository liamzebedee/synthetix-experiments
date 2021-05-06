set -ex


export SYNTHETIX='0x97767D7D04Fd0dB0A1a2478DCd4BA85290556B48'
export ETH_RPC_URL=https://mainnet.infura.io/v3/feb228261711453d992038ab7aebefe3
ACCOUNT=$1
seth call $SYNTHETIX "collateralisationRatio(address _issuer)(uint)" $ACCOUNT