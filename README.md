# count-code-lines
Count code lines in your project

### How use:

1) Clone repository
`git clone https://github.com/webkadiz/count-code-lines.git`
2) `cd count-code-lines`
3) Run command. For example `./ccl ../../Projects/my-favorite-project`
4) Watch on result



### More examples:

```
This will search in two directories 
./ccl some-project-dir-inner1,some-project-dir-inner2

This will exlude following folders: build, static, fonts, config
./ccl --blackbox build,static,fonts,config some-project-dir

This add .vue files in watched
./ccl --ext .vue some-project-dir

This print help
./ccl --help
```
