console.log("[+]Working...")

Java.perform(function(){

    var main = Java.use("com.example.hookman.MainActivity")

    main.isRoot.implementation = function(){
        return Java.use('java.lang.Boolean').valueOf(false);
    }
    console.log("[+]root check bypassed")
    main.isRunningInEmulator.implementation = function(){
        return Java.use("java.lang.Boolean").valueOf(false)
    }
    console.log("[+]emulator check bypass")
    main.check_flag.implementation = function(encryptedFlag){

        var flag = this.encryptedFlag
        var real_flag = this.decryptFlag(flag.value)
        console.log("[+]Flag: "+real_flag)

    }


})
