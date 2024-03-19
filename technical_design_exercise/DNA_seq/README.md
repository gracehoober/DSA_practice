 You are tasked with creating an entry and reporting system for a scientific
 laboratory that specializes in DNA sequencing.

 A DNA sequence is an arbitrarily large list of an exact and ordered
          combination of the following four distinct nucleic acids:
              A - adenine C - cytosine G - guanine T - thymine

 An example DNA sequence for a specimen can be expressed as the following string :
               AAAGTCTGA


 Write a software object model (with methods, functions, etc.)
 that supports the following features:
           a. Entry of a specimen's DNA sequence. The software needs to support
               multiple specimens and multiple sequencing of a specific specimen.
               The order of the nucleic acids is critical to capture.
           b. Data access/storage methods to commit data and then subsequently
               retrieve it from an external data store of your choosing
               (a database, flat file, document store, etc.)
           c. Search for records in three different ways
                   i. via specimen
                   ii. via a DNA sequence string
                   iii. via the date of the sequencing