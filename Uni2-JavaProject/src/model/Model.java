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
            String url = "jdbc:mysql://192.168.72.34:3306/diy_garage";
            String user = "root";
            String password = "uni2";
            conn = DriverManager.getConnection(url, user, password);
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }

        return conn;

    }

    public ArrayList<NewReservation> selectAllReservations() {

        ArrayList<NewReservation> reservations = new ArrayList<>();

        String sql = "SELECT * FROM reservation Where Date >= CAST(CURRENT_TIMESTAMP AS DATE) AND Hour >= CAST(CURRENT_TIMESTAMP AS TIME) ORDER BY Date";

        try (Connection conn = this.connect();
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

        try (Connection conn = this.connect();
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

    public ArrayList<NumberOfReservation> getNumberOfReservationsCabin() {

        ArrayList<NumberOfReservation> reservationsNum = new ArrayList<>();

        String sql = "SELECT Hour, COUNT(Cabin_ID) FROM reservation ORDER BY Hour ";

        try (Connection conn = this.connect();
                Statement stmt = conn.createStatement();
                ResultSet rs = stmt.executeQuery(sql)) {

            // loop through the result set
            while (rs.next()) {

                NumberOfReservation r = new NumberOfReservation(rs.getTime("Hour"), rs.getInt("COUNT(Cabin_ID)"));

                reservationsNum.add(r);
            }
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
        return reservationsNum;
    }

    public void drawGraphicBase(Graphics g, int y2) {
        g.clearRect(40, 100, 900, 900);
        //g.drawRect(40, 100, 300, 300);
        g.setColor(Color.BLACK);
        g.drawLine(100, 200, 100, 400);
        g.drawLine(100, 400, y2, 400);
    }

    public void drawReport1(Graphics g, ArrayList<NumberOfReservation> getNumberOfReservationsCabin) {
        g.setColor(Color.BLACK);
        drawGraphicBase(g, 850);
        //Months
        String[] hours = {"00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00"};

        int maxReservations = 0;

        int x = 100;
        if (getNumberOfReservationsCabin != null) {
            //Draw months
            for (int i = 0; i < hours.length; i++) {
                if (i == 0) {
                    x += 10;
                } else {
                    x += 65;
                }
                g.drawString(hours[i], x, 420);

                //Max income
                if (getNumberOfReservationsCabin.get(i).getNumberOfReservations() > maxReservations) {
                    maxReservations = (int) getNumberOfReservationsCabin.get(i).getNumberOfReservations();
                }

            }

            //Selling income
            g.setColor(Color.BLUE);
            x = 120;
            try {
                for (int i = 0; i < getNumberOfReservationsCabin.size(); i++) {

                    int y = (getNumberOfReservationsCabin.get(i).getNumberOfReservations() * 200) / maxReservations;

                    x += 65;
                    g.fillRect(x - 65, 400 - y, 20, y);
                    g.drawString(String.valueOf(getNumberOfReservationsCabin.get(i).getNumberOfReservations()), x - 60, 400 - y - 10);
                }
            } catch (Exception e) {
                System.out.println(e);
            }

            //Info
            g.setColor(Color.BLACK);
            g.drawString("MONTHS", 885, 405);
            g.drawString("RENTED HOURS", 50, 190);
        }
    }
}
