/*
 * This software has been developed by Uni2
 * Under the GNU General Public License
 */
package model;

import java.util.ArrayList;
import javax.swing.table.AbstractTableModel;
import model.Model;
/**
 *
 * @author rodriguez.markel
 */
public class ProductSoldTable extends AbstractTableModel{
    public ArrayList<ProductSold> product = new ArrayList<>();
    public final String[] columnName = {"Client_DNI, Product_ID, Amount, Date, Hour, Total_price"};


      
    

    public ProductSoldTable(ArrayList<ProductSold> products){
        this.product = products;
     
    }
     
    @Override
    public int getRowCount() {
        return product.size();
    }

    @Override
    public int getColumnCount() {
        return columnName.length;
    }
   
    @Override
    public String getColumnName(int column){
        return columnName[column];
    }
   
    @Override
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

