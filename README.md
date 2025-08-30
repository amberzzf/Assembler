This is my super basic assembler that I made due to my combines interest in my first years systems1 and theory2 module which delved into assembly language and the language acceptance procedure 

Although this may seem like a tedious and unnecessary project, I took interest in the stages of compilation and would consider making a high level translator for a new language in the future (despite its uselessness) 

Current limitations:
-Currently has limited memory capacity which could be rectified by using a file instead of a fixed length list.
-Currently jumps are to a certain line (lines starting from 1 onwards) instead of following the standard assembly format where you jump to a section.
eg: 
main: 
  ADD 1
  ADDM 2
  JUMPZ main
This could be easily fixed by detecting when a section is being defined and creating a 2d array holding the sections
eg: [["main", "ADD 1", "ADDM 2", "JUMPZ main"], ["body", etc]]
-Not a limitation but would add register addressing modes

ps: Please replace the file path with your own 
