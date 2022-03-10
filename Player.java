/*
PS4 Problem 4: Player.java

Morgan Contrino and Arman Zarghani-Shiraz (collaborators)
*/

import java.util.*;

public class Player {

    private String name;
   private Card[] hand;
    private int numCards;

//constructor: intializes fields for Player class

    public Player(String name) {
        this.name = name;
        this.hand = new Card[CardMatch.MAX_CARDS];
        this.numCards = 0;

    }

// Accessor Methods: allow user to access private fields 

public String getName() {
    return this.name;
}

public int getNumCards() {
    return this.numCards;
}
 
//toString method: returns Player's name as a string

public String toString() {
    return this.getName();
}

//mutator method addCard: adds specified card to player's hand

public void addCard(Card card) {

    if (card == null || getNumCards() == CardMatch.MAX_CARDS) {
        throw new IllegalArgumentException();
    }
        int i = getNumCards();
            hand[i] = card;
            this.numCards ++;
        }

//getCard: accessor method that returns the card at specified index

public Card getCard(int index) {

    if (index < 0 || index >= numCards) {
        throw new IllegalArgumentException();
    }
    Card card = hand[0];
    for (int i = 0; i < numCards; i++) {
        if (index == i) {
             card = hand[i];
        }
    }
    return card;
}


//getHandValue: accessor method that computes and returns the total value of the player’s current hand

public int getHandValue() {

    int sumCards = 0;
    for (int i = 0; i < numCards; i++) {
        sumCards += hand[i].getValue();
    }

    if (getNumCards() == CardMatch.MAX_CARDS) {
        return sumCards + CardMatch.MAX_CARDS_PENALTY;
    }
    else {
        return sumCards;
    }
}

/*displayHand: accessor method that prints the current contents of the player’s hand, 
preceded by a heading that includes the player’s name
*/

public void displayHand() {
    System.out.println(getName() + "'s hand:");
    //System.out.println("NUM CARDS:" + numCards);
    for (int i = 0; i < numCards; i++) {
        //System.out.println("HAND:" + i);
        System.out.println("  " + i + ": " + hand[i].getColor() + " " + hand[i].getValue());
    }
}

/* removeCard: accessor method that takes an integer index as a parameter and both removes and 
returns the Card at that position of the player’s hand
*/

public Card removeCard(int index) {
    if (index < 0 || index >= numCards) {
        throw new IndexOutOfBoundsException();
    }
    Card lostCard = hand[index];
    if (index != numCards-1) {
        numCards --;
        hand[index] = hand[this.numCards];
        }
    else {
        numCards--;
        hand[numCards] = null;
        
    }
    return lostCard;
    }


/*getPlay: accessor method that determines and returns the number corresponding to the player’s next play
*/
public int getPlay(Scanner scan, Card nextCard) {
    if (nextCard == null || nextCard.getValue() >= CardMatch.MAX_CARDS) {
        System.out.print(getName() + ": number of card to play (-1 to draw)?");
         }

    int nextPlay = scan.nextInt();
    if (nextPlay != -1 && (nextPlay < 0 || nextPlay > hand.length)) {
        System.out.print(getName() + ": number of card to play (-1 to draw)?");
    }
        return nextPlay;
}


} //end of class dont move it
