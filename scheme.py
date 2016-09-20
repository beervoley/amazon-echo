// Basic scheme for your functions. Structure -> intent : name of func, slots : varName, varType
// Have to be downloaded to developer.amazon.com in your skill
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
          "intent" : "whatIsYourName",
          "slots":
         [
           {
             "name" : "nickname",
             "type" : "AMAZON.US_FIRST_NAME"
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
