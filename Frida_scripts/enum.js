console.log("Enumerating methods of MainActivity");
Java.perform(function() {
  const groups = Java.enumerateMethods('*MainActivity*!*');
  console.log(JSON.stringify(groups, null, 2));
});