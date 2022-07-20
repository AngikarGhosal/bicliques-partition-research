# maximal-biclique-enumeration

## Usage Instructions:

### Execution

Run the JAR file with the file containing the adjacency matrix and the type of output required as arguments.

- *standard* - compute all maximal bicliques(MBEA)

`$ java -jar MBEA.jar path_to/filename.txt  _type_`

### Interpreting the output:

`lNode1 lNode2 ... <-> rNode1 rNode2 ...` is a maximal biclique satisfying the conditions.

- lNode_i_ belongs to the left vertex set
- rNode_i_ belongs to the right vertex set

### To test:

Go to the main directory and execute :

`$ java -jar MBEA.jar matrix.txt standard`
```

 
