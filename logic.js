const balanceSteps = (steps) => {
    let userStep = 6
    
    let lastAppended = steps.find(step => {return step.status == userStep});
    let missingSteps = Array.from(Array(userStep), (_,i)=> (i+1).toString()).filter(x => !steps.some(j => j.status === x));
    
    missingSteps.map(status => steps.push({
        ...lastAppended,
        status
    }));

    return steps

};


a = [
    {
        lastUpdate: "2021-12-15 22:19:05",
        state: "Complete",
        status: "6"
    },{
        lastUpdate: "2021-12-15 22:19:05",
        state: "Complete",
        status: "1"
    },
];
 
res = balanceSteps(a);
 
console.log(res)