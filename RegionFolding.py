# insert insert this code into Default (Windows).sublime-keymap:
# [
#     { "keys": ["f5"], "command": "build" },
#     { "keys": ["alt+ctrl+0", "alt+ctrl+9"], "command": "region_fold_all" },
#     { "keys": ["alt+ctrl+9", "alt+ctrl+0"], "command": "region_unfold_all"},
#     { "keys": ["alt+ctrl+2", "alt+ctrl+1"], "command": "region_fold_current"},
#     { "keys": ["alt+ctrl+1", "alt+ctrl+2"], "command": "region_unfold_current"}
# ]

import sublime, sublime_plugin, os, shutil

MARKER_START='{{{'
MARKER_END='}}}'

class RegionFoldAllCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sections = self.view.find_all(MARKER_START)
        sectionStart=[]
        sectionEnd=[]
        sectionLineEnd=[]
        for x in range(len(sections)):
            sectionStart.append(sections[x].begin())
            sectionEnd.append(sections[x].end())
            sectionLineEnd.append(self.view.line(sections[x].end()).end())

        endStart=[]
        endEnd=[]

        ends = self.view.find_all(MARKER_END)
        for x in range(len(ends)):
            endStart.append(ends[x].begin()-1)
            endEnd.append(ends[x].end())

        selection=self.view.sel()[0]
        for x in range(len(sectionStart)):
            content = sublime.Region(sectionLineEnd[x], endStart[x])
            new_content=[content]
            if content.size() > 0:
                new_content = self.view.fold(content)
            self.selection = new_content

class RegionUnfoldAllCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        startpos = self.view.find_all(MARKER_START)
        endpos=[]

        for x in range(len(startpos)):
            startpos[x]=self.view.line(startpos[x].end()).end()

        endpos = self.view.find_all(MARKER_END)
        for x in range(len(startpos)):
            endpos[x]=self.view.line(endpos[x].begin()).begin()

        for x in range( len(endpos)):
            content = sublime.Region(startpos[x], endpos[x])
            new_content=[content]
            if content.size() > 0:
                new_content = self.view.unfold(content)
            self.selection = new_content

class RegionFoldCurrentCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sections = self.view.find_all(MARKER_START)
        sectionStart=[]
        sectionEnd=[]
        sectionLineEnd=[]
        for x in range(len(sections)):
            sectionStart.append(sections[x].begin())
            sectionEnd.append(sections[x].end())
            sectionLineEnd.append(self.view.line(sections[x].end()).end())

        endStart=[]
        endEnd=[]

        ends = self.view.find_all(MARKER_END)
        for x in range(len(ends)):
            endStart.append(ends[x].begin()-1)
            endEnd.append(ends[x].end())

        selection=self.view.sel()[0]
        for x in range(len(sectionStart)):
            if (sectionStart[x] < selection.begin()) and (endEnd[x] > selection.end()):
                content = sublime.Region(sectionLineEnd[x], endStart[x])
                new_content=[content]
                if content.size() > 0:
                    new_content = self.view.fold(content)
                self.selection = new_content

class RegionUnfoldCurrentCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sections = self.view.find_all(MARKER_START)
        sectionStart=[]
        sectionEnd=[]
        sectionLineEnd=[]
        for x in range(len(sections)):
            sectionStart.append(sections[x].begin())
            sectionEnd.append(sections[x].end())
            sectionLineEnd.append(self.view.line(sections[x].end()).end())

        endStart=[]
        endEnd=[]

        ends = self.view.find_all(MARKER_END)
        for x in range(len(ends)):
            endStart.append(ends[x].begin()-1)
            endEnd.append(ends[x].end())

        selection=self.view.sel()[0]
        for x in range(len(sectionStart)):
            if (sectionStart[x] < selection.begin()) and (endEnd[x] > selection.end()):
                content = sublime.Region(sectionLineEnd[x], endStart[x])
                new_content=[content]
                if content.size() > 0:
                    new_content = self.view.unfold(content)
                self.selection = new_content