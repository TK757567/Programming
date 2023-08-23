Java.perform(function(){

    console.log("[+]here we goooo....")
    var main = Java.use("com.example.clickme.MainActivity")
    var classFields = main.class.getDeclaredFields();
    for (var i = 0; i < classFields.length; i++) {
        console.log("Field:", classFields[i]);}
    main.getFlagButtonClick.implementation  = function(view){
        console.log("[+] clicked")
        var flag = this.getFlag()
        this.CLICKS.value=999999999
        console.log("[+] let it be "+flag)

    }
}
)