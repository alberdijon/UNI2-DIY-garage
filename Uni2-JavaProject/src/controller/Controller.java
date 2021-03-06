/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package controller;

import frames.View;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import model.Model;

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
        //GUIaren konponente guztiei gehitu listenerra
        view.ViewLowStock.addActionListener(listener);
        view.BtnPopularItems.addActionListener(listener); 
        view.SoldToday.addActionListener(listener); 
        view.UpcomingReservations.addActionListener(listener); 
        view.PopularCars.addActionListener(listener);
        view.WorkerSalaries.addActionListener(listener);
        view.CustomerList.addActionListener(listener);
        view.BtnWorkerList.addActionListener(listener);
        view.SwToGraphs.addActionListener(listener);
    }
    @Override
    public void actionPerformed(ActionEvent e) {
        String actionCommand = e.getActionCommand();
        //listenerrak entzun dezakeen eragiketa bakoitzeko. Konponenteek 'actionCommad' propietatea daukate
        switch (actionCommand) {
            
            case "SoldToday":
                
                model.selectAllProductSoldToday();
                
                view.ProductSoldToday.setVisible(true);
                
        }
    }
}