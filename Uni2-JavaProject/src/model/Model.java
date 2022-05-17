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
            String url = "jdbc:mysql://192.168.72.34:3306/diy_garage";
            String user = "root";
            String password = "uni2";
            conn = DriverManager.getConnection(url, user, password);
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }

        return conn;

    }

    public ArrayList<LowStockItems> selectLowStock() {
        ArrayList<LowStockItems> lsitem = new ArrayList<>();
        String sql = "SELECT * FROM product Where Stock <= 5  ORDER BY Stock";
        try (Connection conn = this.connect();
                Statement stmt = conn.createStatement();
                ResultSet rs = stmt.executeQuery(sql)) {

            // loop through the result set
            while (rs.next()) {

                LowStockItems r = new LowStockItems(rs.getInt("ID"), rs.getNString("Name"), rs.getNString("Brand"), rs.getInt("Stock"));

                lsitem.add(r);
            }
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
        return lsitem;
    }

    public ArrayList<PopularItems> selectPopularItems() {
        ArrayList<PopularItems> pitems = new ArrayList<>();
        String sql = "SELECT product.ID, product.Name, product.Brand, product.Price "
                + " FROM product "
                + "INNER JOIN shop ON product.ID=shop.Product_ID"
                + "Where Stock <=5"
                + "ORDER BY Stock";
        try (Connection conn = this.connect();
                Statement stmt = conn.createStatement();
                ResultSet rs = stmt.executeQuery(sql)) {

            // loop through the result set
            while (rs.next()) {

                PopularItems r = new PopularItems(rs.getInt("ID"), rs.getNString("Name"), rs.getNString("Brand"), rs.getInt("Stock"));

                pitems.add(r);
            }
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
        return pitems;
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

    public ArrayList<PopularCars> selectPopularCars() {

        ArrayList<PopularCars> pcars = new ArrayList<>();

        String sql = "SELECT * FROM reservation Where Date >= CAST(CURRENT_TIMESTAMP AS DATE) AND Hour >= CAST(CURRENT_TIMESTAMP AS TIME) ORDER BY Date";

        try (Connection conn = this.connect();
                Statement stmt = conn.createStatement();
                ResultSet rs = stmt.executeQuery(sql)) {

            // loop through the result set
            while (rs.next()) {

                PopularCars r = new PopularCars(rs.getString("Brand"), rs.getString("Model"));

                pcars.add(r);
            }
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
        return pcars;
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

    public ArrayList<NumberOfReservation> getNumberOfReservationsCabin1() {

        ArrayList<NumberOfReservation> reservationsNum1 = new ArrayList<>();

        String sql = "SELECT Hour, COUNT(Cabin_ID AS Number_of_reservation_hourly) FROM reservation WHERE Cabin_ID = 1 ORDER BY Hour ";

        try (Connection conn = this.connect();
                Statement stmt = conn.createStatement();
                ResultSet rs = stmt.executeQuery(sql)) {

            // loop through the result set
            while (rs.next()) {

                NumberOfReservation r = new NumberOfReservation(rs.getTime("Hour"), rs.getInt("COUNT(Cabin_ID)"));

                reservationsNum1.add(r);
            }
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
        return reservationsNum1;
    }

    public ArrayList<NumberOfReservation> getNumberOfReservationsCabin2() {

        ArrayList<NumberOfReservation> reservationsNum2 = new ArrayList<>();

        String sql = "SELECT Hour, COUNT(Cabin_ID AS Number_of_reservation_hourly) FROM reservation WHERE Cabin_ID = 2 ORDER BY Hour ";

        try (Connection conn = this.connect();
                Statement stmt = conn.createStatement();
                ResultSet rs = stmt.executeQuery(sql)) {

            // loop through the result set
            while (rs.next()) {

                NumberOfReservation r = new NumberOfReservation(rs.getTime("Hour"), rs.getInt("COUNT(Cabin_ID)"));

                reservationsNum2.add(r);
            }
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
        return reservationsNum2;
    }

    public ArrayList<NumberOfReservation> getNumberOfReservationsCabin3() {

        ArrayList<NumberOfReservation> reservationsNum3 = new ArrayList<>();

        String sql = "SELECT Hour, COUNT(Cabin_ID AS Number_of_reservation_hourly) FROM reservation WHERE Cabin_ID = 3 ORDER BY Hour ";

        try (Connection conn = this.connect();
                Statement stmt = conn.createStatement();
                ResultSet rs = stmt.executeQuery(sql)) {

            // loop through the result set
            while (rs.next()) {

                NumberOfReservation r = new NumberOfReservation(rs.getTime("Hour"), rs.getInt("COUNT(Cabin_ID)"));

                reservationsNum3.add(r);
            }
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
        return reservationsNum3;
    }

}
