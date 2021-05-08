#! /usr/bin/env python3
# coding: utf-8

class Movie:
    def __init__(self):
        self.title = ''
        self.rating = ''
        self.score = ''
        self.vote = ''
        self.director = ''
        self.writter = ''
        self.duration = ''
        self.release_date = ''
        self.release_country = ''
        self.country = ''
        self.location = ''
        self.review = ''
        self.writterfilmographie = []
        self.directorfilmographie = []
        self.budget = ''
        self.opening_weekend = ''
        self.gross = ''
        self.worldwide_gross = ''
        self.runtime = ''
        self.sound_mix = ''
        self.color = ''
        self.aspect_ratio = ''
    
    def __gettitle__(self):
        return self.title 
    
    def __getrating__(self):
        return self.rating

    def __getscore__(self):
        return self.score
    
    def __getvote__(self):
        return self.vote    
    
    def __gettype__(self):
        return self.type
    
    def __getdirector__(self):
        return self.director   
    
    def __getwritter__(self):
        return self.writter
    
    def __getduration__(self):
        return self.duration
    
    def __getrelease_date__(self):
        return self.release_date
 
    def __getrelease_country__(self):
        return self.release_country   
    
    def __getcountry__(self):
        return self.country
    
    def __getlocation__(self):
        return self.location
    
    def __getreview__(self):
        return self.review
    
    def __getwritterfilmographie__(self):
        return self.writterfilmographie
    
    def __getdirectorfilmographie__(self):
        return self.directorfilmographie
        
    def __getbudget__(self):
        return self.budget
    
    def __getopening_weekend__(self):
        return self.opening_weekend
    
    def __getgross__(self):
        return self.gross
    
    def __getworldwide_gross__(self):
        return self.worldwide_gross
    
    def __getruntime__(self):
        return self.runtime
    
    def __getsound_mix__(self):
        return self.sound_mix
    
    def __getcolor__(self):
        return self.color
    
    def __getaspect_ratio__(self):
        return self.aspect_ratio
    
    ## setter
    def __settitle__(self, tag):
        if tag is not None:
            self.title = tag
        else: 
            self.title = 'xxx' 
    
    def __setrating__(self, tag):
        if tag is not None:
            self.rating = tag
        else:
            self.rating = 'xxx'

    def __setscore__(self, tag):
        if tag is not None:
            self.score = tag
        else:
            self.score = 'xxx'
    
    def __setvote__(self, tag):
        if tag is not None:
            self.vote = tag
        else:
            self.vote = 'xxx'   
    
    def __settype__(self, tag):
        if tag is not None:
            self.type = tag
        else:
            self.type = 'xxx'
    
    def __setdirector__(self, tag):
        if tag is not None:
            self.director = tag 
        else:
            self.director = 'xxx' 
    
    def __setwritter__(self, tag):
        if tag is not None:
            self.writter = tag
        else:
            self.writter = 'xxx'
    
    def __setduration__(self, tag):
        if tag is not None:
            self.duration = tag
        else:
            self.duration = 'xxx'
    
    def __setrelease_date__(self, tag):
        if tag is not None:
            self.release_date = tag
        else:
            self.release_date = 'xxx'
    
    def __setrelease_country__(self, tag):
        if tag is not None:
            self.release_country = tag
        else:
            self.release_country = 'xxx'
                
    def __setcountry__(self, tag):
        if tag is not None:
            self.country = tag
        else:
            self.country = 'xxx'
    
    def __setlocation__(self, tag):
        if tag is not None:
            self.location = tag
        else:
            self.location = 'xxx'
    
    def __setreview__(self, tag):
        if tag is not None:
            self.review = tag
        else: 
            self.review = 'xxx'
    
    def __setwritterfilmographie__(self, tag):
        if tag is not None:
            self.writterfilmographie = tag
        else: 
            self.writterfilmographie = 'xxx'
    
    def __setdirectorfilmographie__(self, tag):
        if tag is not None:
            self.directorfilmographie = tag
        else: 
            self.directorfilmographie = 'xxx'
        
    def __setbudget__(self, tag):
        if tag is not None:
            self.budget = tag
        else:
            self.budget = 'xxx'
    
    def __setopening_weekend__(self, tag):
        if tag is not None:
            self.opening_weekend = tag
        else:
            self.opening_weekend = 'xxx'
            
    def __setgross__(self, tag):
        if tag is not None:
            self.gross =tag
        else: 
            self.gross = 'xxx'
    
    def __setworldwide_gross__(self, tag):
        if tag is not None:
            self.worldwide_gross = tag
        else:
            self.worldwide_gross = 'xxx'
    
    def __setruntime__(self, tag):
        if tag is not None:
            self.runtime = tag
        else:
            self.runtime = 'xxx'
    
    def __setsound_mix__(self, tag):
        if tag is not None:
            self.sound_mix = tag
        else:
            self.sound_mix = 'xxx'
    
    def __setcolor__(self, tag):
        if tag is not None:
            self.color = tag
        else:
            self.color = 'xxx'
    
    def __setaspect_ratio__(self, tag):
        if tag is not None:
            self.aspect_ratio = tag
        else:
            self.aspect_ratio = 'xxx'
    
    
        
    