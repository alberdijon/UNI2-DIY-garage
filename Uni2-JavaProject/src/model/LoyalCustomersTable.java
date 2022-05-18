/*
 * This software has been developed by Uni2
 * Under the GNU General Public License
 */
package model;

import java.util.ArrayList;
import javax.swing.table.AbstractTableModel;

/**
 *
<<<<<<< HEAD
 * @author agirrezabala.peru
 */
public class LoyalCustomersTable extends AbstractTableModel {
    private ArrayList<LoyalCustomers> lcustomer = new ArrayList<>();
    private final String[] columnName = {"DNI", "Name", "Surname"};
    public LoyalCustomersTable(ArrayList<LoyalCustomers> mostLoyal){
        this.lcustomer=mostLoyal;
    }
   
    @Override
    public int getRowCount() {
        return lcustomer.size();
=======
 * @author USUARIO
 */
public class LoyalCustomersTable extends AbstractTableModel {
    private ArrayList<LoyalCustomers> lcustomer =new ArrayList<>();
    private final String[] columnName = {"DNI", "Name", "Surname"};
    
    public LoyalCustomersTable(ArrayList<LoyalCustomers> bestcustomer){
        this.lcustomer=bestcustomer;
    }

    @Override
    public int getRowCount() {
       return lcustomer.size();

>>>>>>> 5bca822bb255ef2bfb3f127e1ad7f6745126e8f2
    }

    @Override
    public int getColumnCount() {
        return columnName.length;
    }
<<<<<<< HEAD
    public String getColumnName(int column){
        return columnName[column];
    }

    @Override
    public Object getValueAt(int rowIndex, int columnIndex) {
        
=======

    @Override
    public Object getValueAt(int rowIndex, int columnIndex) {
>>>>>>> 5bca822bb255ef2bfb3f127e1ad7f6745126e8f2
        switch(columnIndex){
            
            case 0: return lcustomer.get(rowIndex).getDni();
            case 1: return lcustomer.get(rowIndex).getName();
            case 2: return lcustomer.get(rowIndex).getSurname();


            default: return null;
        }
<<<<<<< HEAD
        
=======
>>>>>>> 5bca822bb255ef2bfb3f127e1ad7f6745126e8f2
    }
    
}
