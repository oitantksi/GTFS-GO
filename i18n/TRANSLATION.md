# TRANSLATION

Qt and PyQt have useful internationalization tools. This documents clarify usage of them for incoming contributors.

## Tools

- QtLinguist
    - included in Qt
    - Stand-alone app for Windows - https://www.softpedia.com/get/Others/Home-Education/Qt-Linguist.shtml
- pylupdate5
    - included in PyQt5
- lrelease
    - included in Qt

## Translation steps

1. Add language to project file(gtfs_go.pro)
2. Make .ts-file by pylupdate
3. Add translation to .ts-file on QtLinguist
4. Make .qm-fime from .ts-file by lrelease