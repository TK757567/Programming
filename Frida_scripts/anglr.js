Java.perform(function(){

    
    var strcmp = Module.findExportByName(null,"strcmp");
    console.log("find strcmp:",strcmp);
    Interceptor.attach(strcmp,{
        onEnter: function (args) {
            
            if(ptr(args[0]).readCString().indexOf("HTB")>=0){
                console.log(ptr(args[0]).readCString())
                console.log("[*] strcmp (" + ptr(args[0]).readCString() + "," + ptr(args[1]).readCString()+")");
                
                this.ishack = true;
            }   
    }
    })

})
