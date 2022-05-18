/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package model;

import java.awt.Color;
import java.awt.Graphics;
import java.sql.Connection;

import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.sql.Time;
import java.time.LocalDate;
import java.time.YearMonth;

import java.util.ArrayList;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.JFrame;
import javax.swing.JOptionPane;

/**
 *
 * @author rodriguez.markel
 */
public class Model {

    public Connection connect() {
        Connection conn = null;
        try {
            String url = "jdbc:mysql://localhost:3306/garage";
            String user = "root";
            String password = "";
            conn = DriverManager.getConnection(url, user, password);
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }

        return conn;

    }

    public ArrayList<NewReservation> selectAllReservations() {

        ArrayList<NewReservation> reservations = new ArrayList<>();

        String sql = "SELECT * FROM reservation Where Date >= CAST(CURRENT_TIMESTAMP AS DATE) AND Hour >= CAST(CURRENT_TIMESTAMP AS TIME) ORDER BY Date";

        try (Connection conn = connect();
                Statement stmt = conn.createStatement();
                ResultSet rs = stmt.executeQuery(sql)) {

            // loop through the result set
            while (rs.next()) {

                NewReservation r = new NewReservation(rs.getInt("Cabin_ID"), rs.getString("Client_DNI"), rs.getTime("Hour"), rs.getDate("Date"), rs.getInt("Total"));

                reservations.add(r);
            }
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
        return reservations;
    }

    public ArrayList<ProductSold> selectAllProductSoldToday() {

        ArrayList<ProductSold> products = new ArrayList<>();

        String sql = "SELECT Client_DNI, Product_ID, Amount, Date, Hour, Total_price FROM shop Where Date = CAST(CURRENT_TIMESTAMP AS DATE)";

        try (Connection conn = connect();
                Statement stmt = conn.createStatement();
                ResultSet rs = stmt.executeQuery(sql)) {

            // loop through the result set
            while (rs.next()) {

                ProductSold p = new ProductSold(rs.getString("Client_DNI"), rs.getInt("Product_ID"), rs.getInt("Amount"), rs.getDate("Date"), rs.getTime("Hour"), rs.getInt("Total_price"));

                products.add(p);

            }
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
        return products;

    }
   
      public int getNumberOfReservationsCabin(int month) {
        int year = LocalDate.now().getYear();
        YearMonth yearMonthObject = YearMonth.of(year,month);
        int daysInMonth = yearMonthObject.lengthOfMonth();
         
        int reservations = 0;
        String cadena = "";
        String sql = "SELECT( SELECT COUNT(Date) FROM reservation WHERE Date BETWEEN '"+year+"-"+month+"-01' AND '"+year+"-"+month+"-" + daysInMonth + "') AS 'Reservation_Month' ";
        try (Connection conn = connect();
                Statement stmt = conn.createStatement();
                ResultSet rs = stmt.executeQuery(sql)) {

            // loop through the result set
            while (rs.next()) {
              reservations = rs.getInt("Reservation_Month");
               




            }
        } catch (Exception ex) {
            JOptionPane.showMessageDialog(null, ex.getMessage());
        }
        
        return reservations;

    }
    
    public  Double bookingsMonthD(int month){
        int year = LocalDate.now().getYear();

        YearMonth yearMonthObject = YearMonth.of(year,month);
        int daysInMonth = yearMonthObject.lengthOfMonth();
        String sql = "SELECT (SELECT SUM(Total) FROM reservation WHERE Date BETWEEN '"+year+"-"+month+"-01' AND '"+year+"-"+month+"-" + daysInMonth + "') AS 'Facturation_Month'";

        double total = 0;
        String cadena = "";
        

        try (Connection conn = connect();
                Statement stmt = conn.createStatement();
                ResultSet rs = stmt.executeQuery(sql)) {
            while (rs.next()) {
                total = rs.getDouble("Facturation_Month");

            }
        } catch (Exception ex) {
            JOptionPane.showMessageDialog(null, ex.getMessage());
        }
        return total;
    }
    
     public int drawAllProductSoldToday(String model) {

        int sold = 0;

        String sql = "SELECT (SELECT COUNT(Product_ID) FROM shop CAST(CURRENT_TIMESTAMP AS DATE)) AS 'Sold_Today'";

        try (Connection conn = connect();
                Statement stmt = conn.createStatement();
                ResultSet rs = stmt.executeQuery(sql)) {

            // loop through the result set
            while (rs.next()) {

               sold = rs.getInt("Sold_Today");

                

            }
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
        return sold;

    }
}
  
    
    

