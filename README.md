# RegionFolding-sublimePlugin

I apologize to the author of this plugin.
A couple of years ago I Remodel this plug-in for my needs.
But I do not remember from which source I took the plug-in.
Therefore, I can not provide a link to the source.

# INSTRUCTION

insert insert this code into Default (Windows).sublime-keymap:
[
 { "keys": ["f5"], "command": "build" },
 { "keys": ["alt+ctrl+0", "alt+ctrl+9"], "command": "region_fold_all" },
 { "keys": ["alt+ctrl+9", "alt+ctrl+0"], "command": "region_unfold_all"},
 { "keys": ["alt+ctrl+2", "alt+ctrl+1"], "command": "region_fold_current"},
 { "keys": ["alt+ctrl+1", "alt+ctrl+2"], "command": "region_unfold_current"}
]