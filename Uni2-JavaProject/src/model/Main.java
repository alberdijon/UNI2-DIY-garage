/*
 * This software has been developed by Uni2
 * Under the GNU General Public License
 */
package model;

import frames.View;

/**
 *
 * @author garate.erlantz
 */
public class Main {
    public static void main(String[] args) {
        View frame = new View();
        frame.setTitle("DIY Garage");
        frame.setVisible(true);
        frame.setResizable(false);
    }
}
