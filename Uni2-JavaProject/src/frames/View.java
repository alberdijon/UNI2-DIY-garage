/*
 * This software has been developed by Uni2
 * Under the GNU General Public License
 */
package frames;

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
        PopularCars = new javax.swing.JButton();
        WorkerSalaries = new javax.swing.JButton();
        CustomerList = new javax.swing.JButton();
        jPanel4 = new javax.swing.JPanel();
        jLabel2 = new javax.swing.JLabel();
        SwToGraphs = new javax.swing.JButton();
        jLabelConnection = new javax.swing.JLabel();
        jPanel5 = new javax.swing.JPanel();
        LowStock = new javax.swing.JInternalFrame();
        jScrollPane1 = new javax.swing.JScrollPane();
        jTable1 = new javax.swing.JTable();
        PopularItems = new javax.swing.JInternalFrame();
        jScrollPane2 = new javax.swing.JScrollPane();
        jTable2 = new javax.swing.JTable();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setTitle("DIY Garage");
        setCursor(new java.awt.Cursor(java.awt.Cursor.DEFAULT_CURSOR));
        setResizable(false);
        getContentPane().setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());

        jPanel3.setBackground(new java.awt.Color(204, 204, 255));
        jPanel3.setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());

        jLabel1.setBackground(new java.awt.Color(255, 204, 255));
        jLabel1.setFont(new java.awt.Font("Segoe UI", 0, 18)); // NOI18N
        jLabel1.setForeground(new java.awt.Color(0, 0, 0));
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
        jPanel3.add(UpcomingReservations, new org.netbeans.lib.awtextra.AbsoluteConstraints(10, 240, 180, 40));

        PopularCars.setBackground(new java.awt.Color(153, 153, 255));
        PopularCars.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        PopularCars.setForeground(new java.awt.Color(51, 51, 51));
        PopularCars.setText("Most popular cars");
        PopularCars.setActionCommand("PopularCars");
        PopularCars.setBorderPainted(false);
        jPanel3.add(PopularCars, new org.netbeans.lib.awtextra.AbsoluteConstraints(10, 290, 180, 40));

        WorkerSalaries.setBackground(new java.awt.Color(153, 153, 255));
        WorkerSalaries.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        WorkerSalaries.setForeground(new java.awt.Color(51, 51, 51));
        WorkerSalaries.setText("Employee of the month");
        WorkerSalaries.setBorderPainted(false);
        jPanel3.add(WorkerSalaries, new org.netbeans.lib.awtextra.AbsoluteConstraints(10, 340, 180, 40));

        CustomerList.setBackground(new java.awt.Color(153, 153, 255));
        CustomerList.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        CustomerList.setForeground(new java.awt.Color(51, 51, 51));
        CustomerList.setText("Most loyal customers");
        CustomerList.setActionCommand("CustomerList");
        CustomerList.setBorderPainted(false);
        jPanel3.add(CustomerList, new org.netbeans.lib.awtextra.AbsoluteConstraints(10, 390, 180, 40));

        getContentPane().add(jPanel3, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 0, 200, 500));

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

        jLabelConnection.setForeground(new java.awt.Color(102, 102, 102));
        jLabelConnection.setText("Connecting...");
        jLabelConnection.setHorizontalTextPosition(javax.swing.SwingConstants.LEFT);
        jPanel4.add(jLabelConnection, new org.netbeans.lib.awtextra.AbsoluteConstraints(340, 20, -1, -1));

        getContentPane().add(jPanel4, new org.netbeans.lib.awtextra.AbsoluteConstraints(200, 0, 620, 50));

        jPanel5.setBackground(new java.awt.Color(255, 255, 255));
        jPanel5.setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());

        LowStock.setTitle("Low stock items");
        LowStock.setToolTipText("");
        LowStock.setVisible(false);
        LowStock.getContentPane().setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());

        jScrollPane1.setBorder(null);

        jTable1.setModel(new javax.swing.table.DefaultTableModel(
            new Object [][] {
                {null, null, null, null},
                {null, null, null, null},
                {null, null, null, null},
                {null, null, null, null}
            },
            new String [] {
                "ID", "Name", "Brand", "Stock"
            }
        ) {
            boolean[] canEdit = new boolean [] {
                false, false, false, false
            };

            public boolean isCellEditable(int rowIndex, int columnIndex) {
                return canEdit [columnIndex];
            }
        });
        jScrollPane1.setViewportView(jTable1);

        LowStock.getContentPane().add(jScrollPane1, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 0, 600, 410));

        jPanel5.add(LowStock, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 0, 620, 450));

        PopularItems.setTitle("Popular items");
        PopularItems.setToolTipText("");
        PopularItems.setVisible(false);
        PopularItems.getContentPane().setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());

        jScrollPane2.setBorder(null);

        jTable2.setModel(new javax.swing.table.DefaultTableModel(
            new Object [][] {
                {null, null, null, null, null},
                {null, null, null, null, null},
                {null, null, null, null, null},
                {null, null, null, null, null}
            },
            new String [] {
                "ID", "Name", "Brand", "Sales this month", "Price"
            }
        ) {
            boolean[] canEdit = new boolean [] {
                false, false, false, false, false
            };

            public boolean isCellEditable(int rowIndex, int columnIndex) {
                return canEdit [columnIndex];
            }
        });
        jTable2.setToolTipText("");
        jScrollPane2.setViewportView(jTable2);
        if (jTable2.getColumnModel().getColumnCount() > 0) {
            jTable2.getColumnModel().getColumn(0).setResizable(false);
            jTable2.getColumnModel().getColumn(1).setResizable(false);
            jTable2.getColumnModel().getColumn(2).setResizable(false);
            jTable2.getColumnModel().getColumn(3).setResizable(false);
            jTable2.getColumnModel().getColumn(4).setResizable(false);
        }
        jTable2.getAccessibleContext().setAccessibleName("");

        PopularItems.getContentPane().add(jScrollPane2, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 0, 600, 410));

        jPanel5.add(PopularItems, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 0, 620, 450));

        getContentPane().add(jPanel5, new org.netbeans.lib.awtextra.AbsoluteConstraints(200, 50, 620, 450));

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
    }//GEN-LAST:event_SoldTodayActionPerformed

    private void BtnWorkerListActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_BtnWorkerListActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_BtnWorkerListActionPerformed

    private void BtnPopularItemsActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_BtnPopularItemsActionPerformed
        HideRest();
        PopularItems.setVisible(true);
    }//GEN-LAST:event_BtnPopularItemsActionPerformed
    
    private void HideRest() {
        LowStock.setVisible(false);
        PopularItems.setVisible(false);
    }
    
    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(View.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(View.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(View.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(View.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new View().setVisible(true);

            }
        });
    }
    

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton BtnPopularItems;
    private javax.swing.JButton BtnWorkerList;
    private javax.swing.JButton CustomerList;
    private javax.swing.JInternalFrame LowStock;
    private javax.swing.JButton PopularCars;
    private javax.swing.JInternalFrame PopularItems;
    private javax.swing.JButton SoldToday;
    private javax.swing.JButton SwToGraphs;
    private javax.swing.JButton UpcomingReservations;
    private javax.swing.JButton ViewLowStock;
    private javax.swing.JButton WorkerSalaries;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JLabel jLabelConnection;
    private javax.swing.JPanel jPanel3;
    private javax.swing.JPanel jPanel4;
    private javax.swing.JPanel jPanel5;
    private javax.swing.JScrollPane jScrollPane1;
    private javax.swing.JScrollPane jScrollPane2;
    private javax.swing.JTable jTable1;
    private javax.swing.JTable jTable2;
    // End of variables declaration//GEN-END:variables
}
