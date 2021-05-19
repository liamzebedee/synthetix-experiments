import fetch from 'node-fetch';

async function run() {

    function buildQuery(skip: number) {
        return `{ 
            activeStakers(first:1000, skip:${skip}) { 
                id 
            } 
        }`
    }

    let skip = 0
    let stakers = []
    while (1) {
        let res = await fetch("https://api.thegraph.com/subgraphs/name/synthetixio-team/synthetix", {
            "credentials": "omit",
            "headers": {
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:88.0) Gecko/20100101 Firefox/88.0",
                "Accept": "*/*",
                "Accept-Language": "en-US,en;q=0.5",
                "Content-Type": "application/json"
            },
            "referrer": "https://thegraph.com/",
            "body": JSON.stringify({
                query: buildQuery(skip),
                variables: null
            }),
            "method": "POST",
            "mode": "cors"
        })
        res = await res.json()

        if (res.errors) {
            // console.error(res.error)
            break
            throw null
        }
        if (!res.data) {
            console.error(res)
            throw null
        }
        const { data: { activeStakers } } = res

        if (activeStakers.length == 0) {
            break
        }

        console.log(activeStakers)
        stakers = [...stakers, ...activeStakers]
        skip += 1000
    }

    console.log(JSON.stringify(stakers))

}

run().then(_ => console.log('done')).catch(ex => {
    throw ex
})
