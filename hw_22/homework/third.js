function minimumNumberOfReamsOfPaper (sheetsInReamPaper, consumptionPerWeek, weeksAmount) {
    // count the amount of paper that will go away for all the time
    let consumptionForPeriod = weeksAmount * consumptionPerWeek
    // find the required number of packs
    return (consumptionForPeriod % sheetsInReamPaper) ? (consumptionForPeriod - consumptionForPeriod % sheetsInReamPaper) / sheetsInReamPaper + 1 : consumptionForPeriod / sheetsInReamPaper
}

/*
minimumNumberOfReamsOfPaper(500, 1200, 8)
20
 */