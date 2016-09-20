{
  "intents":
    [
        {
            "intent": "MyMoodIntent",
            "slots":
            [
                {
                "name" : "mood",
                "type" : "LIST_OF_MOODS"
                }
            ]
        }, {
            "intent": "whatIsMyTempIntent"
            }, {
             "intent" : "ifHungry",
                "slots" :
                [
                    {
                    "name" : "hunger",
                    "type" : "LIST_OF_HUNGERS"
                    }
                ]
                },{

            "intent" : "AMAZON.StopIntent"
            }, {
            "intent" : "MyTempIntent",
            "slots" :
            [
                {
                "name" : "newTemp",
                "type" : "LIST_OF_NUMBERS"
                }
            ]
            }
    ]

}
