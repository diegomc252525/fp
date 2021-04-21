#import("dart:io"); 

main() { 
    var stream = new StringInputStream(stdin); 
    stream.onLine =() { 
    var line = stream.readLine(); 
    if (line != null) { 
     print(line); 
    } 
    }; 
}