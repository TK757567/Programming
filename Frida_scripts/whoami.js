console.log("Statring...")
Java.perform(function(){

    var FLAG = Java.use("com.cybertalents.ohmyroot.FLAGbox")
    FLAG.onCreate.implementation = function(){
        var flag = this.DoSomeMagic()
        console.log(flag)
    }



})
Java.perform(function(){
    var IsRooted = Java.use('com.cybertalents.ohmyroot.IsRooted')
    IsRooted.detectTestKeys.overload().implementation = function(){
        return false
    };
    IsRooted.checkForSuBinary.overload().implementation = function(){
        return false

    };
    IsRooted.checkSuExists.overload().implementation  =function(){
        return false
    };
    IsRooted.checkForBusyBoxBinary.overload().implementation = function(){
        return false
    }
    
})



