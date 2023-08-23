console.log("Working...")

Java.perform(function(){

    /*var main =Java.use("com.rloura.pedometer.MainActivity")
    var cFunctionData = JSON.stringify(main.v, null, 2);
    var data = Memory.readByteArray(ptr(0xed92bbf0), 2000);
    console.log(data)
    console.log("Data of c function:", cFunctionData);
    var classes = main.class.getDeclaredFields();
    for (var i = 0;i<classes.length;i++){
        console.log(classes[i])
        }*/
    
    
    var main=Java.use("com.rloura.pedometer.MainActivity")
    var classFields = main.class.getDeclaredFields();
    main.onCreate.implementation = function(bundle){

        var cFunction = this.v;
        
        console.log("Calling c function:", cFunction);
        
        

    }


})