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
import java.util.Date;
/**
 *
 * @author rodriguez.markel
 */
public class Model {
        
    public String driver = "com.mysql.jdbc.Driver";
    public String url = "jdbc:mysql://localhost:3306/garage";
    public String username = "root";
    public String password = "";
 
    public Connection connect() {
        // SQLite connection string
        
        Connection conn = null;
        try {
            Class.forName(driver);
            conn = DriverManager.getConnection(url,username,password);
        } catch (ClassNotFoundException | SQLException e) {
            e.printStackTrace();
        }
        return conn;
    }

    public void selectAllReservations() {
        String sql = "SELECT Cabin-ID, Client-DNI, Hour, Date, Total FROM cabin_client";

        try (Connection conn = this.connect();
                Statement stmt = conn.createStatement();
                ResultSet rs = stmt.executeQuery(sql)) {

            // loop through the result set
            while (rs.next()) {
                System.out.println(rs.getInt("Cabin-ID") +  "\t" + 
                                   rs.getInt("Client-DNI") + "\t" +
                                   rs.getString("Hour") + "\t" +
                                   rs.getString("Date") + "\t" +
                                   rs.getString("Total"));
            }
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
    }
    
    public void selectAllProductSoldToday() {
        
        Date today = new Date();
        
        
        
        String sql = "SELECT Client-DNI, Product-ID, Amount, Date, Hour, Total_price FROM shop WHERE Date = " + today;

        try (Connection conn = this.connect();
                Statement stmt = conn.createStatement();
                ResultSet rs = stmt.executeQuery(sql)) {
                Object[] rows;
            // loop through the result set
            while (rs.next()) {
                rows = new Object[]{rs.getInt("Client-DNI"),rs.getInt("Product-ID"),rs.getString("Amount"),rs.getString("Date"),rs.getString("Hour"),rs.getString("Total_price")};
               
            }
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
    }

}