# Distributed-Systems-PA-2

Nathan Woo and Colin Brush

Design: We followed all of the inital design requirements of the Maekawa's algorithm. A brief description of what thie program does:
 - It finds partitions based on the number of participating processes, and prints the subsets
 - It allows processes to enter critical sections, by first requiring an ack from each other process in the subset
 - This is implemented with a priority queue of the requests, and each process will vote on the requests by sending an ack to the requesting process
 - A process that receives acks from each other process in the subset, can enter the critical section.
 - It will print the vector timestamps of the process as any of the vector clocks are updated
 - It will log all the send and received messages to and from each process to debug_log.log
 
Assumptions:
 - This is a remote algorithm, and mulitple processes will be running on different machines. 
 - The IP addresses of all machines will be known prior to runtime, and will be consistent between all running procesess.

Running:
### To demonstrate running of the program, it is best done with a demo, which is highly recommended.
 - To run, you can start by initializing a Maekawa class, then calling the global initialize function. All processes must do this.
 - Then each individual process can run Maekawa.MInitalize(), to initalize the mutex. Then, calling MLockMutex() will request a lock, while MReleaseMutex() will release the lock on the mutex. Put the critical section inbetween the MLockMutex() and MReleaseMutex(). Then, to finish the process, call MCleanup() and QuitAndCleanup() to cleanup the process. 
 - You will have to define the IP Adresses of all processes you want to run.
 - There are sample runs in main.py and main2.py. If you want to compile the library, and install the library locally with pip that is an option as well. 
 - To build the library and use it locally: `python3 DAP2/setup.py bdist_wheel`, then run `pip3 install dist/DAP2_BrushWoo-0.1.0-py3-none-any.whl` to get the library locally, and you can easily reference the classes and functions within the library.

