# asynchronous vs synchronous

- asynchronous: start a task and move on to next, check back later when the old task is done
- synchronous: wait for something to finish, then move on to start with the next

usually in programming we want things to be async

# synchronous input/output

- early computers were designed to be synchronous
- basically the caller/client sends a request and then blocks other processes/code executions
- once receiver/server responds, the caller/client will unblock
- basically the client and server are in sync

# async i/o

- caller sends request and can work on others until it gets response
- a question that rises: how does caller know it has a response?
  - **epoll**: high performance I/O event notification mechanism in linux-based systems. a way for programs to monitor multiple I/O sources for events without needing to continuously poll (check) each source individually, thus saving CPU cycles.
    - **node.js** has a non-blocking I/O model similar to epoll by default, and plenty other languages/frameworks have their own similar mechanisms
