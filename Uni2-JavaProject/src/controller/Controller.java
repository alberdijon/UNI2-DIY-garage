/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package controller;

import frames.View;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.beans.PropertyVetoException;
import java.util.ArrayList;
import java.util.logging.Level;
import java.util.logging.Logger;
import model.EmployeeOfTheMonth;
import model.EmployeeOfTheMonthTable;
import model.LowStockItems;
import model.LowStockItemsTable;
import model.LoyalCustomers;
import model.LoyalCustomersTable;
import model.Model;
import model.NewReservation;
import model.NewReservationTable;
import model.PopularCars;
import model.PopularCarsTable;
import model.PopularItems;
import model.PopularItemsTable;
import model.ProductSold;
import model.ProductSoldTable;

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
        view.BtnPopularCars.addActionListener(listener);
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
                
                
                
                view.ProductSoldToday.setVisible(true);
                
                ArrayList <ProductSold> product = model.selectAllProductSoldToday();
                view.ProductSold.setModel(new ProductSoldTable(model.selectAllProductSoldToday()));
                
          
                view.ProductSoldToday.setClosable(true);
                

                
            case "UpcomingReservations":
                view.NewReservations.setVisible(true);
                
                ArrayList <NewReservation> reservation = model.selectAllReservations();
                view.Reservations.setModel(new NewReservationTable(model.selectAllReservations()));
                
                view.NewReservations.setClosable(true);
            
                
            case "LowStockItems":
                view.LowStockItemTable.setVisible(true);
                ArrayList <LowStockItems> lsitem = model.selectLowStock();
                view.LowStockItemTable.setModel(new LowStockItemsTable(model.selectLowStock()));
                
                //view.NewReservations.setClosable(true);
            case "PopularItems":
                view.PopularItemsTable.setVisible(true);
                ArrayList <PopularItems> pitems = model.selectPopularItems();
                view.PopularItemsTable.setModel(new PopularItemsTable(model.selectPopularItems()));
                
                //view.
            
            case "PopularCars":
                view.PopularCarsTable.setVisible(true);
                ArrayList <PopularCars> pcars=model.selectPopularCars();
                view.PopularCarsTable.setModel(new PopularCarsTable(model.selectPopularCars()));
                
                //
            case "WorkerSalaries":
                view.EmployeeMonthTable.setVisible(true);
                ArrayList <EmployeeOfTheMonth> memployee=model.selectEmployeeOfTheMonth();
                view.EmployeeMonthTable.setModel(new EmployeeOfTheMonthTable(model.selectEmployeeOfTheMonth()));
            case "CustomerList":
                view.LoyalCustomersTable.setVisible(true);
                ArrayList <LoyalCustomers> lcustomer=model.selectLoyalCustomers();
                view.LoyalCustomersTable.setModel(new LoyalCustomersTable(model.selectLoyalCustomers()));

        }
    }
}
