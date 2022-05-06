/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package model;

import java.sql.Connection;


import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

import java.util.ArrayList;



/**
 *
 * @author rodriguez.markel
 */
public class Model {

 
 
    public Connection connect() {
        Connection conn = null;
        try {
            String url = "jdbc:mysql://localhost:3306/diy_garage";
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
        
        String sql = "SELECT * FROM reservations Where Date >= CAST(CURRENT_TIMESTAMP AS DATE) AND Hour >= CAST(CURRENT_TIMESTAMP AS TIME) ORDER BY Date";
        
        
        
        try (Connection conn = this.connect();
                Statement stmt = conn.createStatement();
                ResultSet rs = stmt.executeQuery(sql)) {

            // loop through the result set
            while (rs.next()) {
                
               NewReservation r = new NewReservation(rs.getInt("Cabin_ID"),rs.getString("Client_DNI"),rs.getTime("Hour"),rs.getDate("Date"),rs.getInt("Total"));
               
               reservations.add(r);
            }
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
        return reservations;
    }
    
    public ArrayList<ProductSold> selectAllProductSoldToday()  {
        

       
       ArrayList<ProductSold> products = new ArrayList<>();
   
        
        String sql = "SELECT Client_DNI, Product_ID, Amount, Date, Hour, Total_price FROM shop Where Date = CAST(CURRENT_TIMESTAMP AS DATE)";
        
        try (Connection conn = this.connect();
                Statement stmt = conn.createStatement();
                ResultSet rs = stmt.executeQuery(sql)) {
                 
            // loop through the result set
            while (rs.next()) {
                
                
               ProductSold p = new ProductSold(rs.getString("Client_DNI"),rs.getInt("Product_ID"),rs.getInt("Amount"),rs.getDate("Date"),rs.getTime("Hour"),rs.getInt("Total_price"));
               
               products.add(p);
               
               
               
               
            }
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
        return products;
        
    }

    

}