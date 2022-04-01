/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package controller;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import model.Model;
import view.View;

/**
 *
 * @author rodriguez.markel
 */
public class Controller implements ActionListener {
      private Model model;
    private View view;
    public Controller(Model model, View view) {
        this.model = model;
        this.view = view;
        gehituActionListener(this);       
    }    
    private void gehituActionListener(ActionListener listener) {
        
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        
    }
}

