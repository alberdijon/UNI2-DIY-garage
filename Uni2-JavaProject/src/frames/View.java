/*
 * This software has been developed by Uni2
 * Under the GNU General Public License
 */
package frames;

import model.ProductSoldTable;
import model.Model;




/**
 *
 * @author Erlantz
 */
public class View extends javax.swing.JFrame {

    /**
     * Creates new form MainFrame
     */
    public View() {
        initComponents();
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jPanel3 = new javax.swing.JPanel();
        jLabel1 = new javax.swing.JLabel();
        BtnWorkerList = new javax.swing.JButton();
        ViewLowStock = new javax.swing.JButton();
        BtnPopularItems = new javax.swing.JButton();
        SoldToday = new javax.swing.JButton();
        UpcomingReservations = new javax.swing.JButton();
        BtnPopularCars = new javax.swing.JButton();
        WorkerSalaries = new javax.swing.JButton();
        CustomerList = new javax.swing.JButton();
        AverageReservations = new javax.swing.JButton();
        jPanel4 = new javax.swing.JPanel();
        jLabel2 = new javax.swing.JLabel();
        SwToGraphs = new javax.swing.JButton();
        jPanel5 = new javax.swing.JPanel();
        LowStock = new javax.swing.JInternalFrame();
        jScrollPane1 = new javax.swing.JScrollPane();
        LowStockItemTable = new javax.swing.JTable();
        PopularItems = new javax.swing.JInternalFrame();
        jScrollPane2 = new javax.swing.JScrollPane();
        PopularItemsTable = new javax.swing.JTable();
        ProductSoldToday = new javax.swing.JInternalFrame();
        jScrollPane3 = new javax.swing.JScrollPane();
        ProductSold = new javax.swing.JTable();
        NewReservations = new javax.swing.JInternalFrame();
        jScrollPane4 = new javax.swing.JScrollPane();
        Reservations = new javax.swing.JTable();
        PopularCars = new javax.swing.JInternalFrame();
        jScrollPane7 = new javax.swing.JScrollPane();
        PopularCarsTable = new javax.swing.JTable();
        ReservationEachHour = new javax.swing.JInternalFrame();
        jScrollPane6 = new javax.swing.JScrollPane();
        ReservationGraphic = new javax.swing.JPanel();
        EmployeeMonth = new javax.swing.JInternalFrame();
        jScrollPane8 = new javax.swing.JScrollPane();
        EmployeeMonthTable = new javax.swing.JTable();
        LoyalCustomers = new javax.swing.JInternalFrame();
        jScrollPane9 = new javax.swing.JScrollPane();
        LoyalCustomersTable = new javax.swing.JTable();
<<<<<<< HEAD
        ProfitsPerMonth = new javax.swing.JInternalFrame();
        jScrollPane10 = new javax.swing.JScrollPane();
        ProfitsPerMonthTable = new javax.swing.JTable();
        LowStock1 = new javax.swing.JInternalFrame();
        jScrollPane5 = new javax.swing.JScrollPane();
        LowStockItemTable1 = new javax.swing.JTable();
=======

        jScrollPane5.setViewportView(jPanel1);
>>>>>>> 5bca822bb255ef2bfb3f127e1ad7f6745126e8f2

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setTitle("DIY Garage");
        setCursor(new java.awt.Cursor(java.awt.Cursor.DEFAULT_CURSOR));
        setResizable(false);
        getContentPane().setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());

        jPanel3.setBackground(new java.awt.Color(204, 204, 255));
        jPanel3.setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());

        jLabel1.setBackground(new java.awt.Color(255, 204, 255));
        jLabel1.setFont(new java.awt.Font("Segoe UI", 0, 18)); // NOI18N
        jLabel1.setHorizontalAlignment(javax.swing.SwingConstants.CENTER);
        jLabel1.setText("[Logo]");
        jLabel1.setOpaque(true);
        jPanel3.add(jLabel1, new org.netbeans.lib.awtextra.AbsoluteConstraints(10, 10, 180, 60));

        BtnWorkerList.setBackground(new java.awt.Color(153, 153, 255));
        BtnWorkerList.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        BtnWorkerList.setForeground(new java.awt.Color(51, 51, 51));
        BtnWorkerList.setText("Profits per month");
        BtnWorkerList.setBorderPainted(false);
        BtnWorkerList.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                BtnWorkerListActionPerformed(evt);
            }
        });
        jPanel3.add(BtnWorkerList, new org.netbeans.lib.awtextra.AbsoluteConstraints(10, 440, 180, 40));

        ViewLowStock.setBackground(new java.awt.Color(153, 153, 255));
        ViewLowStock.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        ViewLowStock.setForeground(new java.awt.Color(51, 51, 51));
        ViewLowStock.setText("Low stock items");
        ViewLowStock.setActionCommand("ViewLessThan5");
        ViewLowStock.setBorderPainted(false);
        ViewLowStock.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                ViewLowStockActionPerformed(evt);
            }
        });
        jPanel3.add(ViewLowStock, new org.netbeans.lib.awtextra.AbsoluteConstraints(10, 90, 180, 40));

        BtnPopularItems.setBackground(new java.awt.Color(153, 153, 255));
        BtnPopularItems.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        BtnPopularItems.setForeground(new java.awt.Color(51, 51, 51));
        BtnPopularItems.setText("Popular items");
        BtnPopularItems.setActionCommand("AllItems");
        BtnPopularItems.setBorderPainted(false);
        BtnPopularItems.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                BtnPopularItemsActionPerformed(evt);
            }
        });
        jPanel3.add(BtnPopularItems, new org.netbeans.lib.awtextra.AbsoluteConstraints(10, 140, 180, 40));

        SoldToday.setBackground(new java.awt.Color(153, 153, 255));
        SoldToday.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        SoldToday.setForeground(new java.awt.Color(51, 51, 51));
        SoldToday.setText("Products sold today");
        SoldToday.setActionCommand("SoldToday");
        SoldToday.setBorderPainted(false);
        SoldToday.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                SoldTodayActionPerformed(evt);
            }
        });
        jPanel3.add(SoldToday, new org.netbeans.lib.awtextra.AbsoluteConstraints(10, 190, 180, 40));

        UpcomingReservations.setBackground(new java.awt.Color(153, 153, 255));
        UpcomingReservations.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        UpcomingReservations.setForeground(new java.awt.Color(51, 51, 51));
        UpcomingReservations.setText("Upcoming reservations");
        UpcomingReservations.setActionCommand("UpcomingReservations");
        UpcomingReservations.setBorderPainted(false);
        UpcomingReservations.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                UpcomingReservationsActionPerformed(evt);
            }
        });
        jPanel3.add(UpcomingReservations, new org.netbeans.lib.awtextra.AbsoluteConstraints(10, 240, 180, 40));

        BtnPopularCars.setBackground(new java.awt.Color(153, 153, 255));
        BtnPopularCars.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        BtnPopularCars.setForeground(new java.awt.Color(51, 51, 51));
        BtnPopularCars.setText("Most popular cars");
        BtnPopularCars.setActionCommand("PopularCars");
        BtnPopularCars.setBorderPainted(false);
        BtnPopularCars.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                BtnPopularCarsActionPerformed(evt);
            }
        });
        jPanel3.add(BtnPopularCars, new org.netbeans.lib.awtextra.AbsoluteConstraints(10, 290, 180, 40));

        WorkerSalaries.setBackground(new java.awt.Color(153, 153, 255));
        WorkerSalaries.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        WorkerSalaries.setForeground(new java.awt.Color(51, 51, 51));
        WorkerSalaries.setText("Employee of the month");
        WorkerSalaries.setBorderPainted(false);
        WorkerSalaries.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                WorkerSalariesActionPerformed(evt);
            }
        });
        jPanel3.add(WorkerSalaries, new org.netbeans.lib.awtextra.AbsoluteConstraints(10, 340, 180, 40));

        CustomerList.setBackground(new java.awt.Color(153, 153, 255));
        CustomerList.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        CustomerList.setForeground(new java.awt.Color(51, 51, 51));
        CustomerList.setText("Most loyal customers");
        CustomerList.setActionCommand("CustomerList");
        CustomerList.setBorderPainted(false);
        CustomerList.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                CustomerListActionPerformed(evt);
            }
        });
        jPanel3.add(CustomerList, new org.netbeans.lib.awtextra.AbsoluteConstraints(10, 390, 180, 40));

        AverageReservations.setBackground(new java.awt.Color(153, 153, 255));
        AverageReservations.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        AverageReservations.setForeground(new java.awt.Color(51, 51, 51));
        AverageReservations.setText("Average of reservations ");
        AverageReservations.setActionCommand("AverageOfReservations ");
        AverageReservations.setBorderPainted(false);
        AverageReservations.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                AverageReservationsActionPerformed(evt);
            }
        });
        jPanel3.add(AverageReservations, new org.netbeans.lib.awtextra.AbsoluteConstraints(10, 490, 180, 40));
        AverageReservations.getAccessibleContext().setAccessibleName("AverageReservations ");

        getContentPane().add(jPanel3, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 0, 200, 650));

        jPanel4.setBackground(new java.awt.Color(204, 204, 255));
        jPanel4.setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());

        jLabel2.setFont(new java.awt.Font("Segoe UI", 0, 18)); // NOI18N
        jLabel2.setForeground(new java.awt.Color(51, 51, 51));
        jLabel2.setHorizontalAlignment(javax.swing.SwingConstants.LEFT);
        jLabel2.setText("Textual reports");
        jPanel4.add(jLabel2, new org.netbeans.lib.awtextra.AbsoluteConstraints(10, 0, 140, 50));

        SwToGraphs.setBackground(new java.awt.Color(255, 204, 255));
        SwToGraphs.setForeground(new java.awt.Color(51, 51, 51));
        SwToGraphs.setText("Switch to graphs");
        SwToGraphs.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                SwToGraphsActionPerformed(evt);
            }
        });
        jPanel4.add(SwToGraphs, new org.netbeans.lib.awtextra.AbsoluteConstraints(440, 10, 170, 30));

        getContentPane().add(jPanel4, new org.netbeans.lib.awtextra.AbsoluteConstraints(200, 0, 620, 50));

        jPanel5.setBackground(new java.awt.Color(255, 255, 255));
        jPanel5.setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());

        LowStock.setBorder(null);
        LowStock.setTitle("Low stock items");
        LowStock.setToolTipText("");
        LowStock.setVisible(false);
        LowStock.getContentPane().setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());

        jScrollPane1.setBorder(null);

        LowStockItemTable.setModel(new javax.swing.table.DefaultTableModel(
            new Object [][] {
                {},
                {},
                {},
                {}
            },
            new String [] {

            }
        ));
        jScrollPane1.setViewportView(LowStockItemTable);

        LowStock.getContentPane().add(jScrollPane1, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 0, 600, 410));

        jPanel5.add(LowStock, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 0, 620, 450));

        PopularItems.setTitle("Popular items");
        PopularItems.setToolTipText("");
        PopularItems.setVisible(false);
        PopularItems.getContentPane().setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());

        jScrollPane2.setBorder(null);

        PopularItemsTable.setModel(new javax.swing.table.DefaultTableModel(
            new Object [][] {
                {},
                {},
                {}
            },
            new String [] {

            }
        ));
        PopularItemsTable.setToolTipText("");
        jScrollPane2.setViewportView(PopularItemsTable);
        PopularItemsTable.getAccessibleContext().setAccessibleName("");

        PopularItems.getContentPane().add(jScrollPane2, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 0, 600, 410));

        jPanel5.add(PopularItems, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 0, 620, 450));

        ProductSoldToday.setTitle("Products sold  today");
        ProductSoldToday.setToolTipText("");
        ProductSoldToday.setVisible(false);
        ProductSoldToday.getContentPane().setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());

        jScrollPane3.setViewportView(ProductSold);

        ProductSoldToday.getContentPane().add(jScrollPane3, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 0, 600, 420));

        jPanel5.add(ProductSoldToday, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 0, 620, 450));

        NewReservations.setTitle("Upcoming Reservations");
        NewReservations.setToolTipText("");
        NewReservations.setVisible(false);
        NewReservations.getContentPane().setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());

        jScrollPane4.setBorder(null);

        Reservations.setModel(new javax.swing.table.DefaultTableModel(
            new Object [][] {

            },
            new String [] {

            }
        ));
        Reservations.setToolTipText("");
        jScrollPane4.setViewportView(Reservations);

        NewReservations.getContentPane().add(jScrollPane4, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 0, 600, 420));

        jPanel5.add(NewReservations, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 0, 620, 450));

<<<<<<< HEAD
=======
        ReservationEachHour.setVisible(false);
        ReservationEachHour.getContentPane().setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());

        jScrollPane6.setViewportView(ReservationGraphic);
        ReservationGraphic.getAccessibleContext().setAccessibleName("ReservationGraphic");

        ReservationEachHour.getContentPane().add(jScrollPane6, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 0, 610, 570));

        jPanel5.add(ReservationEachHour, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 0, 620, 600));
        ReservationEachHour.getAccessibleContext().setAccessibleName("ReservationEachHour");

        PopularCars.setTitle("Popular cars");
>>>>>>> 5bca822bb255ef2bfb3f127e1ad7f6745126e8f2
        PopularCars.setVisible(false);
        PopularCars.getContentPane().setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());

        PopularCarsTable.setModel(new javax.swing.table.DefaultTableModel(
            new Object [][] {
                {},
                {},
                {},
                {}
            },
            new String [] {

            }
        ));
        jScrollPane7.setViewportView(PopularCarsTable);

        PopularCars.getContentPane().add(jScrollPane7, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 0, 500, 380));

        jPanel5.add(PopularCars, new org.netbeans.lib.awtextra.AbsoluteConstraints(270, 220, 620, 450));

        ReservationEachHour.setVisible(false);
        ReservationEachHour.getContentPane().setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());

        jScrollPane6.setViewportView(ReservationGraphic);
        ReservationGraphic.getAccessibleContext().setAccessibleName("ReservationGraphic");

        ReservationEachHour.getContentPane().add(jScrollPane6, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 0, 610, 570));

        jPanel5.add(ReservationEachHour, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 0, 620, 600));
        ReservationEachHour.getAccessibleContext().setAccessibleName("ReservationEachHour");

        EmployeeMonth.setBorder(null);
        EmployeeMonth.setTitle("Employees of the month");
        EmployeeMonth.setVisible(false);

        EmployeeMonthTable.setModel(new javax.swing.table.DefaultTableModel(
            new Object [][] {
                {},
                {},
                {},
                {}
            },
            new String [] {

            }
        ));
        jScrollPane8.setViewportView(EmployeeMonthTable);

        EmployeeMonth.getContentPane().add(jScrollPane8, java.awt.BorderLayout.CENTER);

        jPanel5.add(EmployeeMonth, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 0, 630, 600));

        LoyalCustomers.setBorder(null);
<<<<<<< HEAD
        LoyalCustomers.setTitle("Most Loyal Customers");
=======
        LoyalCustomers.setTitle("Loyal Customers");
>>>>>>> 5bca822bb255ef2bfb3f127e1ad7f6745126e8f2
        LoyalCustomers.setVisible(false);

        LoyalCustomersTable.setModel(new javax.swing.table.DefaultTableModel(
            new Object [][] {
                {},
                {},
                {},
                {}
            },
            new String [] {

            }
        ));
        jScrollPane9.setViewportView(LoyalCustomersTable);

        LoyalCustomers.getContentPane().add(jScrollPane9, java.awt.BorderLayout.CENTER);

        jPanel5.add(LoyalCustomers, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 0, 620, 600));

<<<<<<< HEAD
        ProfitsPerMonth.setBorder(null);
        ProfitsPerMonth.setTitle("Profits per month");
        ProfitsPerMonth.setVisible(false);

        jScrollPane10.setBorder(null);

        ProfitsPerMonthTable.setModel(new javax.swing.table.DefaultTableModel(
            new Object [][] {
                {},
                {},
                {},
                {}
            },
            new String [] {

            }
        ));
        jScrollPane10.setViewportView(ProfitsPerMonthTable);

        ProfitsPerMonth.getContentPane().add(jScrollPane10, java.awt.BorderLayout.CENTER);

        jPanel5.add(ProfitsPerMonth, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 0, 620, 600));

        LowStock1.setBorder(null);
        LowStock1.setToolTipText("Low Stock Items");
        LowStock1.setVisible(false);

        LowStockItemTable1.setModel(new javax.swing.table.DefaultTableModel(
            new Object [][] {
                {},
                {},
                {},
                {}
            },
            new String [] {

            }
        ));
        jScrollPane5.setViewportView(LowStockItemTable1);

        LowStock1.getContentPane().add(jScrollPane5, java.awt.BorderLayout.CENTER);

        jPanel5.add(LowStock1, new org.netbeans.lib.awtextra.AbsoluteConstraints(2, 4, 620, 590));

=======
>>>>>>> 5bca822bb255ef2bfb3f127e1ad7f6745126e8f2
        getContentPane().add(jPanel5, new org.netbeans.lib.awtextra.AbsoluteConstraints(200, 50, 620, 600));

        getAccessibleContext().setAccessibleDescription("");

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void SwToGraphsActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_SwToGraphsActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_SwToGraphsActionPerformed

    private void ViewLowStockActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_ViewLowStockActionPerformed
        HideRest();
        LowStock.setVisible(true);
    }//GEN-LAST:event_ViewLowStockActionPerformed

    private void SoldTodayActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_SoldTodayActionPerformed
        // TODO add your handling code here:
        HideRest();
        ProductSoldToday.setVisible(true);
    }//GEN-LAST:event_SoldTodayActionPerformed

    private void BtnWorkerListActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_BtnWorkerListActionPerformed
        // TODO add your handling code here:
        HideRest();
        ProfitsPerMonth.setVisible(true);
    }//GEN-LAST:event_BtnWorkerListActionPerformed

    private void BtnPopularItemsActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_BtnPopularItemsActionPerformed
        HideRest();
        PopularItems.setVisible(true);
    }//GEN-LAST:event_BtnPopularItemsActionPerformed

    private void UpcomingReservationsActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_UpcomingReservationsActionPerformed
        // TODO add your handling code here:
        HideRest();
        NewReservations.setVisible(true);
    }//GEN-LAST:event_UpcomingReservationsActionPerformed

    private void AverageReservationsActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_AverageReservationsActionPerformed
        // TODO add your handling code here:
        HideRest();
        ReservationEachHour.setVisible(true);
    }//GEN-LAST:event_AverageReservationsActionPerformed

    private void WorkerSalariesActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_WorkerSalariesActionPerformed
        // TODO add your handling code here:
        HideRest();
        EmployeeMonth.setVisible(true);
    }//GEN-LAST:event_WorkerSalariesActionPerformed

    private void BtnPopularCarsActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_BtnPopularCarsActionPerformed
        // TODO add your handling code here:
        HideRest();
        PopularCars.setVisible(true);
    }//GEN-LAST:event_BtnPopularCarsActionPerformed

    private void CustomerListActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_CustomerListActionPerformed
        // TODO add your handling code here:
<<<<<<< HEAD
        HideRest();
        LoyalCustomers.setVisible(true);
=======
>>>>>>> 5bca822bb255ef2bfb3f127e1ad7f6745126e8f2
    }//GEN-LAST:event_CustomerListActionPerformed
    
    private void HideRest() {
        LowStock.setVisible(false);
        PopularItems.setVisible(false);
        NewReservations.setVisible(false);
        ProductSoldToday.setVisible(false);
        ReservationEachHour.setVisible(false);
        PopularCars.setVisible(false);
        EmployeeMonth.setVisible(false);
        LoyalCustomers.setVisible(false);
        ProfitsPerMonth.setVisible(false);
    }
    
    public static View viewaSortuBistaratu() {
        View v = new View();
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                v.setVisible(true);
            }
        });
        return v;
    }
    

    // Variables declaration - do not modify//GEN-BEGIN:variables
    public javax.swing.JButton AverageReservations;
    public javax.swing.JButton BtnPopularCars;
    public javax.swing.JButton BtnPopularItems;
    public javax.swing.JButton BtnWorkerList;
    public javax.swing.JButton CustomerList;
    private javax.swing.JInternalFrame EmployeeMonth;
    public javax.swing.JTable EmployeeMonthTable;
    private javax.swing.JInternalFrame LowStock;
<<<<<<< HEAD
    private javax.swing.JInternalFrame LowStock1;
    private javax.swing.JTable LowStockItemTable;
    public javax.swing.JTable LowStockItemTable1;
=======
    public javax.swing.JTable LowStockItemTable;
>>>>>>> 5bca822bb255ef2bfb3f127e1ad7f6745126e8f2
    private javax.swing.JInternalFrame LoyalCustomers;
    public javax.swing.JTable LoyalCustomersTable;
    public javax.swing.JInternalFrame NewReservations;
    public javax.swing.JInternalFrame PopularCars;
    public javax.swing.JTable PopularCarsTable;
    private javax.swing.JInternalFrame PopularItems;
    public javax.swing.JTable PopularItemsTable;
    public javax.swing.JTable ProductSold;
    public javax.swing.JInternalFrame ProductSoldToday;
    private javax.swing.JInternalFrame ProfitsPerMonth;
    public javax.swing.JTable ProfitsPerMonthTable;
    public javax.swing.JInternalFrame ReservationEachHour;
    public javax.swing.JPanel ReservationGraphic;
    public javax.swing.JTable Reservations;
    public javax.swing.JButton SoldToday;
    public javax.swing.JButton SwToGraphs;
    public javax.swing.JButton UpcomingReservations;
    public javax.swing.JButton ViewLowStock;
    public javax.swing.JButton WorkerSalaries;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JPanel jPanel3;
    private javax.swing.JPanel jPanel4;
    private javax.swing.JPanel jPanel5;
    private javax.swing.JScrollPane jScrollPane1;
    private javax.swing.JScrollPane jScrollPane10;
    private javax.swing.JScrollPane jScrollPane2;
    private javax.swing.JScrollPane jScrollPane3;
    private javax.swing.JScrollPane jScrollPane4;
    private javax.swing.JScrollPane jScrollPane5;
    private javax.swing.JScrollPane jScrollPane6;
    private javax.swing.JScrollPane jScrollPane7;
    private javax.swing.JScrollPane jScrollPane8;
    private javax.swing.JScrollPane jScrollPane9;
    // End of variables declaration//GEN-END:variables
}
