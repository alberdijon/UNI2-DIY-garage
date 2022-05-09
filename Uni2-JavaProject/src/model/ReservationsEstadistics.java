/*
 * This software has been developed by Uni2
 * Under the GNU General Public License
 */
package model;

import java.awt.Graphics2D;

/**
 *
 * @author rodriguez.markel
 */
public class ReservationsEstadistics {
    
     private int x;
     private int y;

    public ReservationsEstadistics() {
        x = 0;
        y = 0;
    }

    public ReservationsEstadistics(int x, int y) {
        this.x = x;
        this.y = y;
    }
    
    public void marraztu(Graphics2D g2d){
        int radioa = 5;
        g2d.fillOval(x, y, radioa, radioa);
        g2d.getTransform();
    }
     
}
