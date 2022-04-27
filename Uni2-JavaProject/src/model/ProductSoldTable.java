/*
 * This software has been developed by Uni2
 * Under the GNU General Public License
 */
package model;

import java.util.ArrayList;
import javax.swing.table.AbstractTableModel;

/**
 *
 * @author rodriguez.markel
 */
public class ProductSoldTable extends AbstractTableModel{
    private ArrayList<ProductSold> product = new ArrayList<>();
    private String[] columnName = {"Client-DNI, Product-ID, Amount, Date, Hour, Total_price"};

     public ProductSoldTable(ArrayList<ProductSold> product){
        this.product = product;
     
    }
     
    public int getRowCount() {
        return product.size();
    }

    public int getColumnCount() {
        return columnName.length;
    }
   
    public String getColumnName(int column){
        return columnName[column];
    }
   
    public Object getValueAt(int rowIndex, int columnIndex) {
       switch(columnIndex){
            case 0: return product.get(rowIndex).getClientDni();
            case 1: return product.get(rowIndex).getProductId();
            case 2: return product.get(rowIndex).getAmount();
            case 3: return product.get(rowIndex).getDate();
            case 4: return product.get(rowIndex).getHour();
            case 5: return product.get(rowIndex).getTotalPrice();
            default: return null;
        }
    }
   
}

