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
            String url = "jdbc:mysql://localhost:3306/garage";
            String user = "root";
            String password = "";
            conn = DriverManager.getConnection(url, user, password);
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }

        return conn;

    }

    public void selectAllReservations() {
        String sql = "SELECT Cabin_ID, Client_DNI, Hour, Date, Total FROM cabin-client";

        try (Connection conn = this.connect();
                Statement stmt = conn.createStatement();
                ResultSet rs = stmt.executeQuery(sql)) {

            // loop through the result set
            while (rs.next()) {
                System.out.println(rs.getInt("Cabin_ID") +  "\t" + 
                                   rs.getString("Client_DNI") + "\t" +
                                   rs.getTime("Hour") + "\t" +
                                   rs.getDate("Date") + "\t" +
                                   rs.getInt("Total"));
            }
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
    }
    
    public void selectAllProductSoldToday() {
        
        
       
       ArrayList<ProductSold> products = new ArrayList<>();
        
        
        String sql = "SELECT Client_DNI, Product_ID, Amount, Date, Hour, Total_price FROM shop ";

        try (Connection conn = this.connect();
                Statement stmt = conn.createStatement();
                ResultSet rs = stmt.executeQuery(sql)) {
                 
            // loop through the result set
            while (rs.next()) {
                
                
                products.add(new ProductSold(rs.getString("Client_DNI"),rs.getInt("Product_ID"),rs.getInt("Amount"),rs.getDate("Date"),rs.getTime("Hour"),rs.getInt("Total_price")));
               
            }
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
    }

    

}