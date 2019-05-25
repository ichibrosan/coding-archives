@echo off
@rem make.bat - 6/2/2010 dwg - 
@rem copyright (c) 2010 douglas goodall. all rights reserved.
@rem
@rem See Borland C++ 4.0 User's Guide pages 177-178...
@rem
@rem -B  build regardless of dependencies   during make
@rem -i  ignore return codes of build tools during make
@rem -m  display date and time of each file during make
@rem -s  suppress on-screen command display during make
@rem 
@maker.exe -B %1
