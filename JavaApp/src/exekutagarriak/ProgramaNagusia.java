/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package exekutagarriak;

import controller.Controller;
import model.Model;
import view.View;

/**
 *
 * @author rodriguez.markel
 */
public class ProgramaNagusia {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
         View view = View.viewaSortuBistaratu();

        Model model = new Model();

        Controller controller = new Controller(model, view);
    }
    
}
