optionDescCarry = "\n\t\t"

helpInfo = [
  {
    "keys": ["-e", "--ext"],
    "desc": "Option's value is a list of extensions with dot separate comma. This files will be" +
            f"{optionDescCarry}counted. By default - [.js]."
  },
  {
    "keys": ["-b", "--blackbox"],
    "desc": "Option's value is a list of files and directories separate comma. This entities will be" +
            f"{optionDescCarry}ignored on all levels. By default - [node_modules]."
  },
  {
    "keys": ["--with-dots"],
    "desc": "This option does not have value. This include files and directories with dot in watched."
  },
  {
    "keys": ["-h", "--help"],
    "desc": "Print help."
  },
  {
    "keys": ["-i", "--include"],
    "desc": "Option's value is a list of files and directories separate comma. This entities will be" +
            f"{optionDescCarry}included in watched. But blackbox have higher priority than include." +
            f"{optionDescCarry}By default - []."
  }
]


def printIndent():
  print("\t", end="")

def printUsage():
  print("Usage:")
  printIndent()
  print("ccl [OPTIONS] PATHS")
  print()
  printIndent()

  print("PATHS - paths to directories which you wish to scan. They separate with comma")
  print()

def printParamsInfo():
  print("OPTIONS:")

  for paramInfo in helpInfo:
    paramKeys = paramInfo["keys"]
    paramDesc = paramInfo["desc"]

    printIndent()
    print(", ".join(paramKeys), ":", sep="")
    printIndent()
    printIndent()
    print(paramDesc)
    print()
  print()

def printExamples():
  print("Examples:")
  printIndent()
  print("ccl some-project-dir")
  print()
  printIndent()
  print("ccl some-project-dir-inner1,some-project-dir-inner2")
  printIndent()
  printIndent()
  print("This will search in two directories")
  print()
  printIndent()
  print("ccl --blackbox build,static,fonts,config some-project-dir")
  printIndent()
  printIndent()
  print("This will exlude following folders: build, static, fonts, config")
  print()
  printIndent()
  print("ccl --ext .vue some-project-dir")
  printIndent()
  printIndent()
  print("This add .vue files in watched")
  
def printHelp():
  printUsage()
  printParamsInfo()
  printExamples()