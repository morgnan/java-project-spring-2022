/*
Morgan Contrino and Arman Zarghani-Shiraz (collaborators)

CS112 PS4 Problem 4: ComputerPlayer.java
ComputerPlayer Class for CardMatch
represents the computer playing against the human player in the CardMatch game
*/

import java.util.*;

public class ComputerPlayer extends Player {

    public ComputerPlayer(String name) {
        super(name);
    }

    public void displayHand() {
        System.out.println(getName() + "'s hand:");
        System.out.println("  " + getNumCards() + " cards");
    }
    
    
    public int getPlay(Scanner scan, Card nextCard) {
        if (nextCard == null || getNumCards() == CardMatch.MAX_CARDS) {
            throw new IllegalArgumentException();
        }

        int score = -1;
        for (int i = 0; i < getNumCards(); i++) {
            if (this.getCard(i).getValue() == nextCard.getValue()) {
                if (this.getCard(i).getValue() > score) {
                    score = i;
                }
            }
            else if (this.getCard(i).getColor() == nextCard.getColor()) {
                    if (this.getCard(i).getValue()  > score) {
                        score = i;
                            }
            }  
    }
    return score;

}
}
