import * as ethers from 'ethers'
import { BigNumber } from 'ethers'
const stakers: [] = require('./data.json')

const one = BigNumber.from(10).pow(18)

async function run() {

    const provider = new ethers.providers.JsonRpcProvider("https://mainnet.infura.io/v3/feb228261711453d992038ab7aebefe3")
    const contract = new ethers.Contract(
        "0x97767D7D04Fd0dB0A1a2478DCd4BA85290556B48",
        // [
        //     "function collateralisationRatio(address _issuer) external view returns (string)",
        // ],
        require("/Users/liamz/Documents/Work/2021_Synthetix/code/synthetix/build/artifacts/contracts/Synthetix.sol/Synthetix.json").abi,
        provider
    )
    
    // process in batches of 16.
    let batches = []
    let batch = []
    const BATCH_SIZE = 512
    stakers.map((curr, i) => {
        if((i % BATCH_SIZE) == 0) {
            batches.push(batch)
            batch = []
        }
        batch.push(curr)
    })

    for(let batch of batches) {
        await Promise.all(batch.map(async ({ id }) => {
            let ratio = await contract.collateralisationRatio(id)
            console.log(`${id},${ethers.utils.formatEther(ratio)}`)
        }))
    }
}


run().then(_ => console.log('done')).catch(ex => {
    throw ex
})
