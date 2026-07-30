# GameSafeLinker

GameSafeLinker is a utility designed to manage game directories or save files using Windows junction points. By creating a directory junction, the tool links a default game folder to a custom destination folder. This is often used to redirect local save games to a cloud storage directory for automatic backups, while the game continues to read and write to its original path.

## Permissions and Security

This program requires administrator rights to run. The Windows operating system restricts the creation of directory junctions to elevated users. Without these permissions, the tool cannot create the necessary folder links.

## Available Versions

| Format | File Extension | Use Case | Prerequisites |
| --- | --- | --- | --- |
| Source Code | .py | Reviewing the code or running the script manually | Python environment installed |
| Standalone | .exe | Quick use without installing any development tools | None |

## How it works

A Windows junction acts like a transparent shortcut for folders. When a game saves progress to its standard folder, Windows automatically redirects the files to the target folder set by GameSafeLinker. This allows the files to be stored safely in a different location without modifying the game itself.
