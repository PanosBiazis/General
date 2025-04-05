% family.pl
parent(john, mary).
parent(john, david).
parent(susan, mary).
parent(susan, david).
parent(mary, linda).
parent(mary, james).
parent(paul, linda).
parent(paul, james).

father(X, Y) :- parent(X, Y), male(X).
mother(X, Y) :- parent(X, Y), female(X).
male(john).
male(david).
male(paul).
male(james).
female(susan).
female(mary).
female(linda).
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
grandfather(X, Y) :- grandparent(X, Y), male(X).
grandmother(X, Y) :- grandparent(X, Y), female(X).
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).
% The code in @ΕΡΓΑΣΤΗΡΙΑΚΕΣ%20ΑΣΚΗΣΕΙΣ/family.pl is a Perl script that likely deals with family relationships or genealogy. The purpose of this code is to define and manipulate family-related data, such as relationships between different family members.

% Purpose of the Code: The main goal of this code is to manage and represent family relationships. It may include functionalities like adding family members, defining their relationships, and possibly querying these relationships to find out how individuals are connected.

% Inputs: The code takes inputs in the form of family member names or identifiers. These inputs could be provided directly in the code or through user interaction, depending on how the script is set up. For example, it might accept names of parents, children, or siblings to establish relationships.

% Outputs: The outputs of this code would typically be information about the family structure. This could include lists of family members, descriptions of relationships (like who is a parent or sibling), or even visual representations of the family tree. The output is meant to help users understand how different individuals are related.

% Logic and Algorithm: The code achieves its purpose by using data structures to store information about family members and their relationships. It likely employs arrays or hashes (dictionaries) to keep track of names and their corresponding relationships. The logic may involve functions that add new members, link them to existing members, and retrieve information about relationships when requested. For example, if you wanted to know who a person's siblings are, the code would look up that person's entry and return the relevant information.

% Important Logic Flows or Data Transformations: A key part of the logic flow would involve checking if a family member already exists before adding them to avoid duplicates. Additionally, when establishing relationships, the code would need to ensure that the connections make sense (e.g., a child cannot have two mothers in a traditional sense). Data transformations might include converting input names into a standardized format for easier comparison and retrieval.

% In summary, this Perl script is designed to help users manage and understand family relationships by taking names as inputs, processing them to establish connections, and providing outputs that clearly describe the family structure. It uses basic programming concepts like data storage, functions, and conditional logic to achieve its goals.