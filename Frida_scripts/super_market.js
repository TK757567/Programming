console.log("hello")
Java.perform(function(){

    var main = Java.use("com.example.supermarket.MainActivity")
    var stringFromJNI = main.stringFromJNI;
    var stringFromJNI2 = main.stringFromJNI2;
    var stringFromJNI3 = main.stringFromJNI3;
    stringFromJNI.implementation = function() {
        var result = this.stringFromJNI(); // Call the original method
        console.log("stringFromJNI() returned:", result);
        return result;
    };
    
    stringFromJNI2.implementation = function(){
        var result = this.stringFromJNI2();
        console.log("res: "+result)
        return result
    

    }

    stringFromJNI3.implementation = function(){
        var res = this.stringFromJNI3();
        console.log("res: "+res)
    }

    
    var new_inst1 = main.$new();
    new_inst1.stringFromJNI();
    new_inst1.stringFromJNI2();
    new_inst1.stringFromJNI3();



})
