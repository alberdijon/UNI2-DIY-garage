/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package controller;

import frames.View;
import java.awt.Graphics;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.beans.PropertyVetoException;
import java.io.File;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import model.Model;
import model.NewReservation;
import model.NewReservationTable;
import model.NumberOfReservation;
import model.ProductSold;
import model.ProductSoldTable;
import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartFrame;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.plot.PlotOrientation;
import org.jfree.data.category.DefaultCategoryDataset;

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
        view.EarningsEachMonth.addActionListener(listener);
        view.AverageReservations.addActionListener(listener);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        String actionCommand = e.getActionCommand();
        //listenerrak entzun dezakeen eragiketa bakoitzeko. Konponenteek 'actionCommad' propietatea daukate
        switch (actionCommand) {

            case "SoldToday":

                view.ProductSoldToday.setVisible(true);

                ArrayList<ProductSold> product = model.selectAllProductSoldToday();
                view.ProductSold.setModel(new ProductSoldTable(model.selectAllProductSoldToday()));

                view.ProductSoldToday.setClosable(true);
               

            case "UpcomingReservations":
                view.NewReservations.setVisible(true);

                ArrayList<NewReservation> reservation = model.selectAllReservations();
                view.Reservations.setModel(new NewReservationTable(model.selectAllReservations()));

                view.NewReservations.setClosable(true);
                

            case "AverageReservations":

                DefaultCategoryDataset ds = new DefaultCategoryDataset();
                ds.addValue(model.getNumberOfReservationsCabin(1), "January", "");
                ds.addValue(model.getNumberOfReservationsCabin(2), "February", "");
                ds.addValue(model.getNumberOfReservationsCabin(3), "March", "");
                ds.addValue(model.getNumberOfReservationsCabin(4), "April", "");
                ds.addValue(model.getNumberOfReservationsCabin(5), "May", "");
                ds.addValue(model.getNumberOfReservationsCabin(6), "June", "");
                ds.addValue(model.getNumberOfReservationsCabin(7), "July", "");
                ds.addValue(model.getNumberOfReservationsCabin(8), "August", "");
                ds.addValue(model.getNumberOfReservationsCabin(9), "September", "");
                ds.addValue(model.getNumberOfReservationsCabin(10), "October", "");
                ds.addValue(model.getNumberOfReservationsCabin(11), "November", "");
                ds.addValue(model.getNumberOfReservationsCabin(12), "December", "");
                JFreeChart jf;
                jf = ChartFactory.createBarChart("The Number of Reservations each hour", "Cuantity", "Month", ds, PlotOrientation.VERTICAL, true, true, true);
                ChartFrame f = new ChartFrame("Graphic", jf);
                f.setSize(1000, 600);
                f.setLocationRelativeTo(null);
                f.setVisible(true);
                

            case "EarnigsEachMonth":

                

                DefaultCategoryDataset ds2 = new DefaultCategoryDataset();
                ds2.addValue(model.bookingsMonthD(1), "January", "");
                ds2.addValue(model.bookingsMonthD(2), "February", "");
                ds2.addValue(model.bookingsMonthD(3), "March", "");
                ds2.addValue(model.bookingsMonthD(4), "April", "");
                ds2.addValue(model.bookingsMonthD(5), "May", "");
                ds2.addValue(model.bookingsMonthD(6), "June", "");
                ds2.addValue(model.bookingsMonthD(7), "July", "");
                ds2.addValue(model.bookingsMonthD(8), "August", "");
                ds2.addValue(model.bookingsMonthD(9), "September", "");
                ds2.addValue(model.bookingsMonthD(10), "October", "");
                ds2.addValue(model.bookingsMonthD(11), "November", "");
                ds2.addValue(model.bookingsMonthD(12), "December", "");

                JFreeChart jf2;
                jf2 = ChartFactory.createBarChart("Bookings", "Comparison between Bookings per Month", "EARNED MONEY", ds2, PlotOrientation.VERTICAL, true, true, true);
                ChartFrame f2 = new ChartFrame("Graphic", jf2);
                f2.setSize(1000, 600);
                f2.setLocationRelativeTo(null);
                f2.setVisible(true);
                
                
        }
    }
}
