# RegionFolding-sublimePlugin

Я взял код с какого-то другого плагина
Regions are those areas of code that are enclosed between markers {{{ & }}}

### Sample

`sample.css`:
```javascript
// {{{ region №1

.block1 { display:inline; height:0px; left:-1000px; }
.block2 { margin: 0px auto; }

// }}}

// {{{ region №2

.content { display:inline; height:0px; left:-1000px; }

// }}}
```

### Default Shortcuts
* Fold all regions with keyboard: _alt + ctrl + 9_
* Unfold all regions with keyboard: _alt + ctrl + 0_
* Fold current region with keyboard: _alt + ctrl + 1_
* Unfold current region with keyboard: _alt + ctrl + 2_

### Settings

insert insert this code into `Default (Linux).sublime-keymap` or `Default (Windows).sublime-keymap`:
```javascript
[
 { "keys": ["alt+ctrl+0", "alt+ctrl+9"], "command": "region_fold_all" },
 { "keys": ["alt+ctrl+9", "alt+ctrl+0"], "command": "region_unfold_all"},
 { "keys": ["alt+ctrl+2", "alt+ctrl+1"], "command": "region_fold_current"},
 { "keys": ["alt+ctrl+1", "alt+ctrl+2"], "command": "region_unfold_current"}
]
```